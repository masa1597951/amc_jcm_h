from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo2_cit', __name__)


@bp.route('/dentista/view/citas', methods=['GET', 'POST'])
@login_required
def view_citas():

        db, c = get_db()
        c.execute(
        'select u.tx_correo, p.tx_nombre, p.tx_paterno, p.tx_materno, c.id_cita, c.fk_id_paciente, c.fh_cita, c.fk_id_dentista '
        'from usuarios u JOIN persona p on u.id_usuario = p.fk_id_usuario '
        'JOIN citas c on u.id_usuario = c.fk_id_paciente where u.id_dentista= %s order by c.fh_cita desc', 
        (g.user['id_usuario'],)     
        )
        citas = c.fetchall()  

        return render_template('todo2/viewcit.html', citas=citas)





