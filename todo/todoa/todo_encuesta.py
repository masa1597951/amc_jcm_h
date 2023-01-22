from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from werkzeug.security import generate_password_hash
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo_encuesta', __name__)


@bp.route('/view/encuesta/graficas')
@login_required
def view_enc_g():
        
    values = [1, 2, 3, 4, 5, 6, 7];
    labels = ["A", "B", "C", "D", "E", "F", "G"];
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"];



    return render_template('todo/viewenc_g.html', title='Gráfica', max=17000, set=zip(values, labels, colors))


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
        'JOIN preguntas p on p.id_pregunta = r.fk_id_pregunta where fk_id_consulta= %s ',
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

        return render_template('todo/viewenc_ind_sp.html', encuestas = encuestas, val = val)