from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from werkzeug.security import generate_password_hash
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo3_encuesta', __name__)


@bp.route('/paciente/view/encuesta')
@login_required
def view_encuesta():

    db, c = get_db()

    c.execute(
        'select * from encuesta e'
        ' JOIN citas c on c.id_cita = e.fk_id_consulta'
        ' where c.fk_id_paciente = %s and e.val = %s',
        (g.user['id_usuario'],False)
    )
    encuestas = c.fetchall()

    return render_template('todo3/view_enc.html', encuestas = encuestas)

def get_consulta(id_consulta):
     db, c = get_db()
     c.execute(
          'select * from consulta where id_consulta = %s', 
          (id_consulta,)
     )
     todo = c.fetchone()

     if todo is None:
          abort(404, "La consulta de id {0} no existe ".format(id_consulta))
     
     return todo

@bp.route('/<int:id_consulta>/paciente/crear/encuesta', methods=['GET', 'POST'])
@login_required
def crear_encuesta(id_consulta):
    consulta= get_consulta(id_consulta)
    db, c = get_db() 
    error = None
    correct = "Encuesta almacenada con éxito"

    c.execute(
        'select * from preguntas'
    )
    preguntas = c.fetchall()

    if request.method == 'POST':

        respuesta1 = request.form.get('p_1')
        respuesta2 = request.form.get('p_2')
        respuesta3 = request.form.get('p_3')
        respuesta4 = request.form.get('p_4')
        respuesta5 = request.form.get('p_5')
        respuesta6 = request.form.get('p_6')
        respuesta7 = request.form.get('p_7')
        respuesta8 = request.form.get('p_8')
        respuesta9 = request.form.get('p_9')
        respuesta10 = request.form.get('p_10')

        if respuesta1 == "0" or respuesta2 == "0" or respuesta3 == "0" or respuesta4 == "0" or respuesta5 == "0" or respuesta6 == "0" or respuesta7 == "0" or respuesta8 == "0" or respuesta9 == "0" or respuesta10 == "0":
            error = "Tienes que responder a todas las preguntas"
            flash(error)
        else:
            
            # pregunta 1
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (1,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta1),id_consulta)
            )  
            db.commit()
            # pregunta 2
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (2,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta2),id_consulta)
            )  
            db.commit()
            # pregunta 3
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (3,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta3),id_consulta)
            )  
            db.commit()
            # pregunta 4
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (4,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta4),id_consulta)
            )  
            db.commit()
            # pregunta 5
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (5,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta5),id_consulta)
            )  

            db.commit()
            # pregunta 6
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (6,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta6),id_consulta)
            )  
            db.commit()
            # pregunta 7
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (7,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta7),id_consulta)
            )  
            db.commit()
            # pregunta 8
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (8,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta8),id_consulta)
            )  
            db.commit()

            # pregunta 9
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s)',
                (9,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta9),id_consulta)
            )  
            db.commit()
            # pregunta 10
            c.execute(
                'insert into respuestas (fk_id_pregunta, fk_id_paciente, fk_id_dentista, nu_resp, fk_id_consulta) '
                'values (%s,%s,%s,%s,%s) ',
                (10,consulta['fk_id_paciente'],consulta['fk_id_dentista'],int(respuesta10),id_consulta)
            )  
            db.commit()

            c.execute(
                'update encuesta set val= %s where fk_id_consulta = %s',
                (True, id_consulta)
            )
            db.commit()

            flash(correct)

            return redirect(url_for('todo3.index'))


    return render_template('todo3/crear_enc.html', preguntas = preguntas)