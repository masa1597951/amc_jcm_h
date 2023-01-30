from flask import(
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort #algun todo que no le pertenezca mandar un abort
from todo.auth import login_required #http para redireccionar si no tiene permiso
from todo.db import get_db

bp = Blueprint('index', __name__)

def get_rol(correo):
    
    db, c = get_db()
    c.execute(
          'select fk_id_rol from usuarios where id_usuario = %s', 
          (correo,)
    )
    id_rol = c.fetchone()

    if id_rol is None:
          abort(404, "El ID del pago {0} no existe ".format(id_rol))

    return id_rol

@bp.route('/<int:correo>/log', methods=['GET','POST'])
def index(correo):
    usuario = get_rol(correo)

    if correo == 1 or correo == "3":
            return redirect(url_for('todo.index'))
    if correo == 2 or correo == "2":
            return redirect(url_for('todo2.index'))
    if correo == 3 or correo == "3":
            return redirect(url_for('todo3.index'))
    else:
            return redirect(url_for('auth.login')) 
   