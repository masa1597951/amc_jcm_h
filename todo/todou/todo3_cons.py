from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo3_cons', __name__)

#Citas
@bp.route('/paciente/expediente', methods=['GET', 'POST'])
@login_required
def view_expediente():

    consultas = None
     
    db, c = get_db()
    c.execute(
        'select c.id_consulta, t.tx_nombre, '
        'c.fk_id_paciente, '
        'd.id_pago, d.nu_total '
        'from consulta c JOIN persona p on c.fk_id_paciente = p.fk_id_usuario '
        'JOIN usuarios u on u.id_usuario = c.fk_id_paciente '
        'JOIN tratamientos t on t.id_tratamiento =  c.fk_id_tratamiento '
        'JOIN pagos d on d.id_pago = c.id_consulta '
        'where u.id_usuario= %s order by u.tx_correo asc', 
        (g.user['id_usuario'],)     
    )
    consultas = c.fetchall() 

    return render_template('todo3/view_cons.html', consultas = consultas)