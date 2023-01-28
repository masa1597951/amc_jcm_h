from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo3_cons', __name__)

@bp.route('/paciente/expediente', methods=['GET', 'POST'])
@login_required
def view_expediente():

    consultas = None
     
    db, c = get_db()
    c.execute(
        'select c.id_consulta, t.tx_nombre, p.id_pago, p.nu_total ,i.fh_cita from consulta c JOIN citas i on i.id_cita = c.id_consulta '
        'JOIN tratamientos t on t.id_tratamiento =  c.fk_id_tratamiento '
        'JOIN pagos p on p.fk_id_paciente = c.fk_id_paciente '
        'where i.fk_id_paciente = %s', 
        (g.user['id_usuario'],)     
    )
    consultas = c.fetchall() 

    return render_template('todo3/view_cons.html', consultas = consultas)

def get_pago(id_pago):
     db, c = get_db()
     c.execute(
          'select * from pagos where id_pago = %s', 
          (id_pago,)
     )
     pago = c.fetchone()

     if pago is None:
          abort(404, "El ID del pago {0} no existe ".format(id_pago))
        
     return pago

@bp.route('/<int:id_pago>/paciente/view/pago', methods=['GET', 'POST'])
@login_required
def view_pagos(id_pago):
    pago = get_pago(id_pago)

    db, c = get_db()
    c.execute(
        'select a.nu_nabono, a.nu_monto, a.fh_abono, p.nu_total ' 
        'from abono a JOIN pagos p on p.id_pago = a.fk_id_pago ' 
        'where fk_id_pago = %s'
        ,(id_pago,)
    )
    pagos = c.fetchall()



    return render_template('todo3/view_pago.html', pagos = pagos)