from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo_mat', __name__)

#Materiales
@bp.route('/createm', methods=['GET', 'POST'])
@login_required
def create_material():
        
        if request.method == 'POST':
                nombre = request.form['nombre']
                cantidad = request.form['cantidad']
            
                db, c = get_db()
                error = None
                c.execute(
                'select tx_nombre from materiales where tx_nombre = %s',(nombre,)
                )
                if not nombre:
                        error = 'El nombre es requerido'
                if not cantidad:
                        error = 'La cantidad es requerida'
                if not cantidad.isnumeric():
                        error = 'Debe de ser un número'

                elif c.fetchone() is not None:
                        error = 'Material {} se encuentra registrado.'.format(nombre)

                if error is None:
                        c.execute(
                                'insert into materiales (tx_nombre, nu_cantidad) values (%s, %s)',
                                (nombre, cantidad)
                        )
                        db.commit()

                        return redirect(url_for('todo.index'))
                
                flash(error)

        return render_template('todo/createm.html')

def get_material(id_material):
     db, c = get_db()
     c.execute(
          'select * from materiales where id_material = %s', 
          (id_material,)
     )
     todo = c.fetchone()

     if todo is None:
          abort(404, "El materiales de id {0} no existe ".format(id_material))
     
     return todo

@bp.route('/<int:id_material>/updatem', methods=['GET', 'POST'])
@login_required
def update_material(id_material):
    todo= get_material(id_material)

    if request.method == 'POST':
          
          nombre = request.form['nombre']
          cantidad = request.form['cantidad']

          error = None
          correct = "Exito al actualizar"

          if not nombre:
               error = "El nombre del material es requerido"
          if not cantidad:
               error = "La cantidad del material es requerida"
          if not cantidad.isnumeric():
                error = 'Debe de ser un número'
              
          if error is None:
               db, c = get_db()
               c.execute(
                    'update materiales set tx_nombre = %s, nu_cantidad = %s where id_material= %s',
                    (nombre, cantidad, id_material)
               )
               db.commit()
               flash(correct)

               return redirect(url_for('todo.index')) 

          flash(error) 
  
    
    return render_template('todo/updatem.html', todo=todo)

@bp.route('/viewm')
@login_required
def view_material():
    
        db, c = get_db()
        c.execute(
        'select id_material, tx_nombre, nu_cantidad from materiales'     
        )
        todos = c.fetchall()  

        return render_template('todo/viewm.html', todos=todos)

@bp.route('/<int:id_material>/delete/material', methods=['POST'])
@login_required
def delete_material(id_material):
     
     correcto = 'Exito al eliminar los datos del material'
     db, c =get_db()
     c.execute('SET FOREIGN_KEY_CHECKS=0')
     c.execute('delete from materiales where id_material = %s',(id_material,))
     c.execute('SET FOREIGN_KEY_CHECKS=1')
     db.commit()
     flash(correcto)
     return redirect(url_for('todo.index'))