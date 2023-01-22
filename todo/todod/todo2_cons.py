from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo2_cons', __name__)


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

def get_cita(id_cita):
     db, c = get_db()
     c.execute(
          'select * from citas where id_cita = %s', 
          (id_cita,)
     )
     todo = c.fetchone()

     if todo is None:
          abort(404, "La cita de id {0} no existe ".format(id_cita))
     
     return todo

@bp.route('/<int:id_usuario>/dentista/view/consulta', methods=['GET', 'POST'])
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


        return render_template('todo2/viewcons.html', consultas=consultas)

@bp.route('/<int:id_cita>/dentista/consulta', methods=['GET', 'POST'])
@login_required
def create_consulta(id_cita):
    cita= get_cita(id_cita)
    db, c = get_db() 
    c.execute(
     'select * from materiales'
     )
    materiales = c.fetchall()

    c.execute(
     'select tx_nombre,id_tratamiento from tratamientos'
     )
    tratamientos = c.fetchall()

    error = None
    correct = "Exito al actualizar"

    if request.method == 'POST':
          action = request.form.get('crear')
          
          if action == "Crear":

               desc = request.form['desc']
               tratamiento = request.form.get('tratamiento')

               if not desc:
                    error = "La descripcion es requerida"
                    flash(error) 

               if not tratamiento:
                    error = "El tratamiento es requerido"
                    flash(error) 

               else:

                    c.execute(
                         'select id_consulta from consulta where id_consulta = %s',
                         (id_cita,)
                    )
                    val_cons = c.fetchone()

                    c.execute(
                         'select id_pago from pagos where id_pago = %s',
                         (id_cita,)
                    )
                    val_pago = c.fetchone()
                    

                    if val_cons is not None or val_pago is not None:
                         error = "Consulta ya creada, por favor selecciona los materiales utilizados en la consulta"
                         flash(error) 

                    else:

                         if error is not None:
                              flash(error)
                         else:
                               c.execute(
                                    'select * from citas where id_cita = %s', 
                                    (id_cita,)
                               )
                               todo = c.fetchone() 

                               c.execute(
                                    'select nu_precio from tratamientos where id_tratamiento = %s', 
                                    (tratamiento,)
                               )
                               pago = c.fetchone()

                               c.execute(
                                    'insert into consulta ( id_consulta , fk_id_paciente , fk_id_dentista, fk_id_tratamiento ,tx_desc ) '
                                    'values (%s, %s, %s, %s, %s) ',
                                    (id_cita, todo['fk_id_paciente'], todo['fk_id_dentista'], tratamiento ,desc)
                               )
                               db.commit()

                               c.execute(
                                   'insert into pagos (id_pago, fk_id_paciente, nu_total) '
                                   'values (%s ,%s , %s)',
                                   (id_cita, todo['fk_id_paciente'] , pago['nu_precio'])
                               )
                               db.commit()

                               c.execute(
                                   'insert into encuesta (fk_id_consulta, val) '
                                   'values(%s,%s)',
                                   (id_cita,False)
                               )
                               db.commit()

                               flash(correct)
          

          elif action == "Agregar":
          
            material  = request.form.get('material')
            cantidad  = request.form['cantidad']

            if not material:
               error = "El material es requerido"

            if not cantidad:
               error = "La cantidad es requerida"

            else:
               c.execute(
                    'update materiales set nu_cantidad= nu_cantidad -%s  where id_material= %s',
                    (cantidad,material)
               )
               db.commit()

               c.execute(
                    'insert into mat_consulta (fk_id_material,fk_id_consulta,nu_cantidad) '
                    'values(%s,%s,%s)',
                    (material,id_cita,cantidad)
               )
               db.commit()

               flash(correct)

          elif action == "Terminar":

               return redirect(url_for('todo2.index'))



    
    return render_template('todo2/create_cons.html',  materiales=materiales, tratamientos=tratamientos)



