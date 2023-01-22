from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from werkzeug.security import check_password_hash, generate_password_hash
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo_den', __name__)

# Dentistas
@bp.route('/created', methods=['GET', 'POST'])
@login_required
def create_dentista():

        db, c = get_db()
        error = None
        c.execute(
                'select id_usuario, tx_correo from usuarios where fk_id_rol = 2'
        )
        dentistas = c.fetchall()

        if request.method == 'POST':
                correo = request.form['correo']
                password = request.form['password']
                nombre = request.form['nombre']
                ap = request.form['ap']
                am = request.form['am']
                telefono = request.form['telefono']
                sexo = request.form['sexo']
                id_dentista = request.form.get('id_dentista')

               
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
                        error = 'ID Dentista es requerido'
                elif c.fetchone() is not None:
                        error = 'Usuario {} se encuentra registrado.'.format(correo)

                if error is None:
                        c.execute(
                                'insert into usuarios (tx_correo, tx_password, fk_id_rol, id_dentista) values (%s, %s, %s, %s)',
                                (correo, generate_password_hash(password), 2, id_dentista)
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

                        return redirect(url_for('todo.index'))
                
                flash(error)
    
        return render_template('todo/created.html', dentistas = dentistas)

@bp.route('/viewd')
@login_required
def view_dentista():
    
        db, c = get_db()
        c.execute(
        'select * from usuarios u JOIN persona p on u.id_usuario = p.fk_id_usuario'
        ' where fk_id_rol = %s order by u.tx_correo asc', (2,)     
        )
        usuarios = c.fetchall() 
        
        return render_template('todo/viewd.html', usuarios=usuarios)

def get_dentista(id_usuario):
     db, c = get_db()
     c.execute(
          'select * from usuarios u JOIN persona p on u.id_usuario = p.fk_id_usuario where u.id_usuario = %s', 
          (id_usuario,)
     )
     usuario = c.fetchone()

     if usuario is None:
          abort(404, "El dentista de id {0} no existe ".format(id_usuario))
        
     return usuario

@bp.route('/<int:id_usuario>/updated', methods=['GET', 'POST'])
@login_required
def update_dentista(id_usuario):
    usuario= get_dentista(id_usuario)

    if request.method == 'POST':

         correo = request.form['correo']
         password = request.form['password']
         nombre = request.form['nombre']
         ap = request.form['ap']
         am = request.form['am']
         telefono = request.form['telefono']
         sexo = request.form['sexo']
         id_dentista = request.form['id_dentista']

         error = None 
         correct = "Exito al actualizar"

         if not correo:
                error = 'Username es requerido'      
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
                error = 'ID Dentista es requerido'
         
         if  error is not None:
                flash(error)
                
         elif not password:
               db, c = get_db()   
               c.execute(
                        'update usuarios set tx_correo =%s, id_dentista =%s where id_usuario =%s',
                        (correo, id_dentista, id_usuario)
               )
               db.commit()
               c.execute(
                        'update persona set tx_nombre =%s , tx_paterno =%s , tx_materno =%s,'
                        ' tx_telefono =%s, tx_sexo =%s where fk_id_usuario =%s',
                        (nombre, ap, am, telefono, sexo, id_usuario)
                )
               db.commit()
           
               flash(correct)
               return redirect(url_for('todo.index'))
         else:     
               db, c = get_db()     
               c.execute(
                        'update usuarios set tx_correo =%s , tx_password =%s , id_dentista =%s where id_usuario =%s',
                        (correo, generate_password_hash(password), id_dentista, id_usuario)
                )
               db.commit()
               c.execute(
                        'update persona set tx_nombre =%s , tx_paterno =%s , tx_materno =%s,'
                        ' tx_telefono =%s, tx_sexo =%s where fk_id_usuario =%s',
                        (nombre, ap, am, telefono, sexo, id_usuario)
                )
               db.commit()
               flash(correct)
               return redirect(url_for('todo.index'))
  
    return render_template('todo/updated.html', usuario=usuario)

@bp.route('/<int:id_usuario>/delete/dentista', methods=['POST'])
@login_required
def delete_usuario(id_usuario):
     
     correcto = 'Exito al eliminar los datos'
     db, c =get_db()
     c.execute('SET FOREIGN_KEY_CHECKS=0')
     c.execute('delete from usuarios where id_usuario = %s',(id_usuario,))
     c.execute('delete from persona where  fk_id_usuario = %s',(id_usuario,))
     c.execute('SET FOREIGN_KEY_CHECKS=1')
     db.commit()
     flash(correcto)
     return redirect(url_for('todo.index'))