from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from werkzeug.security import generate_password_hash

bp = Blueprint('chatbot', __name__)

@bp.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    val = " Para más información, porfavor consulta con nuestros expertos "
    r1 = "Puedes encontrar personal disponible para atenderte en un horario de 09:00 a 14:00 y de 15:00 a 18:00 de Lunes a Viernes."
    r2 = "Puedes encontrarnos en Av. Té 950, Granjas México, Iztacalco, Ciudad de México."
    r3 = "Hola, Buen día!"
    r4 = "Los costos varian dependiendo el tratamiento a realizar. "
    r5 = "Para agendar una cita, consulte a su Dentista para ver la disponibilidad."
    r6 = "Para tener una consulta, debe de estar previamente registrado en nuestra pagina. Asista directamente a la clínica o llame al número +52 5581262942 para darle más información al respecto. "
    r7 = "No tengo una respuesta precisa para tu pregunta, sin embargo, puedes ponerte en contacto con nuestros expertos para mayor información al +52 5581262942"

    if request.method == 'POST':

        pregunta = request.form['desc']

        if pregunta.find('Horarios') >= 0 or pregunta.find('horarios') >= 0:
            val = r1
        if pregunta.find('Ubicacion') >= 0 or pregunta.find('ubicacion') >= 0:
            val = r2
        if pregunta.find('Hola') >= 0 or pregunta.find('hola') >= 0:
            val = r3
        if pregunta.find('Costos') >= 0 or pregunta.find('costos') >= 0:
            val = r4
        if pregunta.find('Citas') >= 0 or pregunta.find('citas') >= 0:
            val = r5
        if pregunta.find('Consulta') >= 0 or pregunta.find('consulta') >= 0:
            val = r6
        if pregunta.find('Dientes') >= 0 or pregunta.find('dientes') >= 0:
            val = r7
    return render_template('authless/chat_bot.html',val = val)

@bp.route('/')
def init():
    return render_template('authless/indexs.html')
    
