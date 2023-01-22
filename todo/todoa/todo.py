from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from werkzeug.security import check_password_hash, generate_password_hash
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('todo', __name__)

@bp.route('/indexa')
@login_required
def index():

    return render_template('todo/index.html')
