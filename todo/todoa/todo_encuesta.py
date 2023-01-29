from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect, jsonify
)
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo_encuesta', __name__)


@bp.route('/view/encuesta/graficas')
@login_required
def view_enc_g():

    malo = 0
    regular = 0
    bueno = 0
    mbueno = 0

    maloc = 0
    regularc = 0
    buenoc = 0
    mbuenoc = 0

    db, c = get_db()
    c.execute(
        'select nu_resp from respuestas where fk_id_pregunta between 1 and 5'
    )
    encuestas = c.fetchall() 
    
    for encuesta in encuestas:
                if encuesta['nu_resp'] == 1:
                    malo = malo + 1 
                if encuesta['nu_resp'] == 2:
                    regular = regular + 1  
                if encuesta['nu_resp'] == 3:
                    bueno = bueno + 1
                if encuesta['nu_resp'] == 4:
                    mbueno = mbueno + 1

    c.execute(
        'select nu_resp from respuestas where fk_id_pregunta between 6 and 10'
    )
    encuestasc = c.fetchall() 
    
    for encuestac in encuestasc:
                if encuestac['nu_resp'] == 1:
                    maloc = maloc + 1 
                if encuestac['nu_resp'] == 2:
                    regularc = regularc + 1  
                if encuestac['nu_resp'] == 3:
                    buenoc = buenoc + 1
                if encuestac['nu_resp'] == 4:
                    mbuenoc = mbuenoc + 1

    data = {'Task' : 'Satisfaccion', 'Malo' : malo, 'Regular' : regular, 'Bueno' : bueno, 'Muy Bueno' : mbueno}

    datac = {'Task' : 'Satisfaccion', 'Malo' : maloc, 'Regular' : regularc, 'Bueno' : buenoc, 'Muy Bueno' : mbuenoc}


    return render_template('todo/viewenc_g.html',data=data, datac=datac)


@bp.route('/<id_usuario>/view/encuestas/individual')
@login_required
def view_enc_ind(id_usuario):
        
        db, c = get_db()
        c.execute(
        'select distinct(r.fk_id_consulta), c.id_cita, c.fh_cita from respuestas r '
        'JOIN citas c on r.fk_id_consulta = c.id_cita where r.fk_id_paciente = %s ',
        (id_usuario,)
        )
        encuestas = c.fetchall() 

        return render_template('todo/viewenc_ind.html', encuestas = encuestas)

@bp.route('/<fk_id_consulta>/view/encuesta/individual')
@login_required
def view_enc_ind_sp(fk_id_consulta):
        
        db, c = get_db()
        c.execute(
        'select r.fk_id_consulta, r.nu_resp, r.fk_id_pregunta, p.tx_pregunta from respuestas r '
        'JOIN preguntas p on p.id_pregunta = r.fk_id_pregunta where r.fk_id_consulta= %s ',
        (fk_id_consulta,)
        )
        encuestas = c.fetchall() 

        val = []

        for encuesta in encuestas:
                if encuesta['nu_resp'] == 1:
                    val.append("malo")
                if encuesta['nu_resp'] == 2:
                    val.append("regular")
                if encuesta['nu_resp'] == 3:
                    val.append("bueno")
                if encuesta['nu_resp'] == 4:
                    val.append("muy bueno")

        return render_template('todo/viewenc_ind_sp.html', encuestas = encuestas, val = val, fk_id_consulta = fk_id_consulta)

@bp.route('/<int:fk_id_consulta>/delete/encuesta', methods=['POST'])
@login_required
def delete_encuesta(fk_id_consulta):
     
     correcto = 'Exito al eliminar los datos de la encuesta'
     db, c =get_db()
     c.execute('SET FOREIGN_KEY_CHECKS=0')
     c.execute('delete from respuestas where fk_id_consulta = %s',(fk_id_consulta,))
     c.execute('update encuesta set val=%s where fk_id_consulta= %s',(0,fk_id_consulta))
     c.execute('SET FOREIGN_KEY_CHECKS=1')
     db.commit()
     flash(correcto)
     return redirect(url_for('todo.index'))