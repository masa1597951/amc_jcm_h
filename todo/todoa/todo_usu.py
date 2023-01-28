from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from werkzeug.security import generate_password_hash
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo_usu', __name__)

#Usarios
@bp.route('/createu', methods=['GET', 'POST'])
@login_required
def create_usuario():

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

                        return redirect(url_for('todo.index'))
                
                flash(error)
    
        return render_template('todo/createu.html', dentistas = dentistas)

@bp.route('/viewu')
@login_required
def view_usuario():
    
        db, c = get_db()
        c.execute(
        'select * from usuarios u JOIN persona p on u.id_usuario = p.fk_id_usuario'
        ' where fk_id_rol = %s order by u.tx_correo asc', (3,)     
        )
        usuarios = c.fetchall() 
        

        return render_template('todo/viewu.html', usuarios=usuarios)

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

@bp.route('/<int:id_usuario>/updateu',  methods=['GET', 'POST'])
@login_required
def update_usuario(id_usuario):
    usuario= get_usuario(id_usuario)

    db, c = get_db()
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
         if id_dentista == "empty":
                id_dentista = usuario['id_dentista']
         
         if  error is not None:
                flash(error)
                
         elif not password:
               db, c = get_db()
               c.execute('SET FOREIGN_KEY_CHECKS=0')    
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
               c.execute('SET FOREIGN_KEY_CHECKS=1') 
               db.commit()
           
               flash(correct)
               return redirect(url_for('todo.index'))
         else:     
               db, c = get_db() 
               c.execute('SET FOREIGN_KEY_CHECKS=0')     
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
               c.execute('SET FOREIGN_KEY_CHECKS=0') 
               db.commit()
               flash(correct)
               return redirect(url_for('todo.index'))
  
    return render_template('todo/updateu.html', usuario=usuario, dentistas=dentistas)

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


@bp.route('/<int:id_usuario>/view/consulta', methods=['GET', 'POST'])
@login_required
def view_consultas(id_usuario):
        usuario= get_usuario(id_usuario)
     
        db, c = get_db()
        c.execute(
        'select u.tx_correo, p.tx_nombre as nomus, p.tx_paterno, p.tx_materno, c.id_consulta, t.tx_nombre, '
        'c.fk_id_paciente, c.tx_desc, c.fk_id_dentista, '
        'd.id_pago, d.nu_total '
        'from consulta c JOIN persona p on c.fk_id_paciente = p.fk_id_usuario '
        'JOIN usuarios u on u.id_usuario = c.fk_id_paciente '
        'JOIN tratamientos t on t.id_tratamiento =  c.fk_id_tratamiento '
        'JOIN pagos d on d.id_pago = c.id_consulta '
        'where u.id_usuario= %s order by u.tx_correo asc', 
        (id_usuario,)     
        )
        consultas = c.fetchall() 

        return render_template('todo/viewcons.html', consultas=consultas)


@bp.route('/<int:id_usuario>/delete/paciente', methods=['POST'])
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

def get_consulta(id_consulta):
     db, c = get_db()
     c.execute(
          'select * from consulta where id_consulta = %s', 
          (id_consulta,)
     )
     consulta = c.fetchone()

     if consulta is None:
          abort(404, "La consulta de id {0} no existe ".format(id_consulta))
        
     return consulta

@bp.route('/<int:id_consulta>/update/consulta', methods=['GET', 'POST'])
@login_required
def update_consulta(id_consulta):
    todo= get_consulta(id_consulta)

    if request.method == 'POST':
          
          desc = request.form['desc']

          error = None
          correct = "Exito al actualizar"

          if not desc:
               error = "La cantidad del material es requerida"

          if  error is not None:
              flash(error) 
          else:
               db, c = get_db()
               c.execute(
                    'update consulta set tx_desc = %s where id_consulta= %s',
                    ( desc, id_consulta )
               )
               db.commit()
          flash(correct)
               
          return redirect(url_for('todo.index'))   
    
    return render_template('todo/updatecons.html', todo=todo)

@bp.route('/<int:id_consulta>/delete/consulta', methods=['POST'])
@login_required
def delete_consulta(id_consulta):
     
     correcto = 'Exito al eliminar los datos de la consulta'
     db, c =get_db()
     c.execute('SET FOREIGN_KEY_CHECKS=0')
     c.execute('delete from consulta where id_consulta = %s',(id_consulta,))
     c.execute('SET FOREIGN_KEY_CHECKS=1')
     db.commit()
     flash(correcto)
     return redirect(url_for('todo.index'))

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

@bp.route('/<int:id_pago>/view/pago', methods=['GET', 'POST'])
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



    return render_template('todo/view_pago.html', pagos = pagos)