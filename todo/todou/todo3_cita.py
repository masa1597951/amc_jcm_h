
from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo3_cita', __name__)

#Citas
@bp.route('/paciente/cita', methods=['GET', 'POST'])
@login_required
def create_cita():
        
        if request.method == 'POST':
                fecha = request.form['fecha']
                hora = request.form['hora']
                datetime = fecha + ' ' + hora + ':00'

                db, c = get_db()
                error = None
                correcto = 'Cita Agendada Correctamente'
                c.execute(
                 'select fh_cita, fk_id_dentista from citas where fh_cita = %s and fk_id_dentista = %s'
                 ,(datetime, g.user['id_dentista'])
                 )
                if not fecha:
                         error = 'Fecha es requerida'
                if not hora:
                        error = 'Hora es requerido'

                elif c.fetchone() is not None:
                         error = 'Hora o Fecha no disponible' + datetime

                if error is None:
                         c.execute(
                                 'insert into citas (fk_id_paciente, fh_cita, fk_id_dentista) '
                                 'values (%s, %s, %s)',
                                 (g.user['id_usuario'], datetime, g.user['id_dentista'])
                         )
                         db.commit()
                         flash(correcto)
                         return redirect(url_for('todo3.index'))
                
                flash(error)

        return render_template('todo3/create_cita.html')