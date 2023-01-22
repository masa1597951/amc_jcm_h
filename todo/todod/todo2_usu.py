from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from werkzeug.security import generate_password_hash
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo2_usu', __name__)

@bp.route('/dentista/create/paciente', methods=['GET', 'POST'])
@login_required
def create_usuario():
        if request.method == 'POST':
                correo = request.form['correo']
                password = request.form['password']
                nombre = request.form['nombre']
                ap = request.form['ap']
                am = request.form['am']
                telefono = request.form['telefono']
                sexo = request.form['sexo']
                id_dentista = g.user['id_usuario']
                db, c = get_db()
                error = None
                c.execute(
                'select id_usuario from usuarios where tx_correo = %s',(correo,)
                )
                if not correo:
                        error = 'Username es requerido'
                if not password:
                        error = 'Password es requerido'
                if not nombre:
                        error = 'Nombre es requerido'
                if not ap:
                        error = 'Apellido Paterno es requerido'
                if not am:
                        error = 'Apellido Materno es requerido'
                if not telefono:
                        error = 'Telefono es requerido'
                if not sexo:
                        error = 'Sexo es requerido'
                if not id_dentista:
                        error = 'ID dentista es requerido'

                elif c.fetchone() is not None:
                        error = 'Usuario {} se encuentra registrado.'.format(correo)

                if error is None:
                        c.execute(
                                'insert into usuarios (tx_correo, tx_password, fk_id_rol, id_dentista) values (%s, %s, %s, %s)',
                                (correo, generate_password_hash(password), 3, id_dentista)
                        )
                        c.execute(
                                'SET FOREIGN_KEY_CHECKS=0'
                        )
                        c.execute(
                                'insert into persona (tx_nombre, tx_paterno, tx_materno, tx_telefono, tx_sexo) values (%s, %s, %s, %s, %s)',
                                (nombre, ap, am, telefono, sexo)
                        )
                        c.execute(
                                'SET FOREIGN_KEY_CHECKS=1'
                        )
                        db.commit()

                        return redirect(url_for('todo2.index'))
                
                flash(error, id_dentista)
    
        return render_template('todo2/createu.html')

@bp.route('/dentista/view/pacientes')
@login_required
def view_usuario():
    
        db, c = get_db()
        c.execute(
        'select * from usuarios u JOIN persona p on u.id_usuario = p.fk_id_usuario'
        ' where u.fk_id_rol = %s and u.id_dentista = %s order by u.tx_correo asc', (3, g.user['id_usuario'])     
        )
        usuarios = c.fetchall() 

        return render_template('todo2/viewu.html', usuarios=usuarios)

def get_usuario(id_usuario):
     db, c = get_db()
     c.execute(
          'select * from usuarios u JOIN persona p on u.id_usuario = p.fk_id_usuario where u.id_usuario = %s', 
          (id_usuario,)
     )
     usuario = c.fetchone()

     if usuario is None:
          abort(404, "El dentista de id {0} no existe ".format(id_usuario))
        
     return usuario

@bp.route('/<int:id_usuario>/dentista/cita',  methods=['GET', 'POST'])
@login_required
def create_cita(id_usuario):
    usuario= get_usuario(id_usuario)

    if request.method == 'POST':
                fecha = request.form['fecha']
                hora = request.form['hora']
                datetime = fecha + ' ' + hora + ':00'

                db, c = get_db()
                error = None
                correcto = 'Cita Agendada Correctamente '
                c.execute(
                 'select fh_cita, fk_id_dentista from citas where fh_cita = %s and fk_id_dentista = %s'
                 ,(datetime, g.user['id_usuario'])
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
                        (id_usuario , datetime , g.user['id_usuario'])
                        )
                        db.commit()
                        flash(correcto)
                        return redirect(url_for('todo2.index'))
                
                flash(error)

    return render_template('todo2/create_cita.html', usuario=usuario)