import functools

from flask import(
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)
# flash es para mandar mensajes  de error de autenticacion y poder ser interceptados por las plantillas

from werkzeug.security import check_password_hash, generate_password_hash #encriptar y checar contraseñas

from todo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        nombre = request.form['nombre']
        ap = request.form['ap']
        am = request.form['am']
        telefono = request.form['telefono']
        sexo = request.form['sexo']

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

        elif c.fetchone() is not None:
            error = 'Usuario {} se encuentra registrado.'.format(correo)

        if error is None:
            c.execute(
                'insert into usuarios (tx_correo, tx_password, fk_id_rol) values (%s, %s, %s)',
                (correo, generate_password_hash(password), 3)
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

            return redirect(url_for('auth.login'))
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute (
            'select * from usuarios where tx_correo = %s', (correo,)
        )
        user = c.fetchone()

        if user is None:
            error = 'Usuario y/o Contraseña inválida'
        elif not check_password_hash(user['tx_password'], password):
            error = 'Usuario y/o Contraseña inválida'    

        if error is None:
            session.clear()
            session['id_usuario'] = user['id_usuario']
            
            if user['fk_id_rol'] is 1:
                return redirect(url_for('todo.index'))
            if user['fk_id_rol'] is 2:
                return redirect(url_for('todo2.index'))
            if user['fk_id_rol'] is 3:
                return redirect(url_for('todo3.index'))
            else:
                return redirect(url_for('todo3.index'))   
        
        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    id_usuario = session.get('id_usuario')

    if id_usuario is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            'select * from usuarios where id_usuario = %s', (id_usuario,)
        )
        g.user = c.fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)
    
    return wrapped_view

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))