from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo2_pago', __name__)


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

@bp.route('/<int:id_pago>/dentista/pago', methods=['GET', 'POST'])
@login_required
def add_pago(id_pago):
    usuario = get_pago(id_pago)

    db, c = get_db()
    c.execute(
        'select nu_total, fk_id_paciente from pagos where id_pago = %s'
        ,(id_pago,)
    )
    pago = c.fetchone()

    if request.method == 'POST':
                fecha = request.form['fecha']
                abono = request.form['abono']

                error = None
                correcto = 'Pago Realizado Correctamente '
                
                if not fecha:
                         error = 'Fecha es requerida'
                if not abono:
                        error = 'Abono requerido'

                if error is None:
                        c.execute(
                           'select max(nu_nabono) as num from abono where fk_id_pago = %s ',
                           (id_pago,)    
                        )
                        nu_nabono = c.fetchone()
                        
                        if nu_nabono is None:
                            num = 1 #numero del abono
                        else:
                            num = sum(nu_nabono.values()) + 1

                        c.execute(
                        'insert into abono (fk_id_pago, fk_id_paciente, nu_nabono, nu_monto, fh_abono) '
                        'values (%s, %s, %s, %s, %s)',
                        (id_pago, pago['fk_id_paciente'], num ,abono, fecha)
                        )
                        db.commit()
                        flash(correcto)
                        return redirect(url_for('todo2.index'))
                

                flash(error)

    return render_template('todo2/add_pago.html', pago = pago)


@bp.route('/<int:id_pago>/dentista/view/pago', methods=['GET', 'POST'])
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



    return render_template('todo2/view_pago.html', pagos = pagos)

