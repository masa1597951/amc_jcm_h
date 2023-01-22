from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from werkzeug.security import generate_password_hash
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo2_encuesta', __name__)


@bp.route('/dentista/create/encuesta')
@login_required
def create_enc():

        correcto = 'Encuesta creada con exito'
        flash(correcto)

        return render_template('todo2/index.html',)