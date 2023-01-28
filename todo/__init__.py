import os
from  flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = 'mikey',
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE = os.environ.get('FLASK_DATABASE'),
    )
    #exportar todas las variables en la consola de comandos
    
    from . import db

    db.init_app(app)

    from . import auth, chatbot
    from .todoa import todo, todo_mat, todo_den, todo_usu, todo_encuesta
    from .todod import todo2, todo2_usu, todo2_cit, todo2_cons, todo2_pago, todo2_encuesta
    from .todou import todo3, todo3_cita, todo3_encuesta, todo3_cons

    app.register_blueprint(auth.bp)
    app.register_blueprint(chatbot.bp)

    app.register_blueprint(todo.bp)
    app.register_blueprint(todo_mat.bp)
    app.register_blueprint(todo_den.bp)
    app.register_blueprint(todo_usu.bp)
    app.register_blueprint(todo_encuesta.bp)

    app.register_blueprint(todo2.bp)
    app.register_blueprint(todo2_usu.bp)
    app.register_blueprint(todo2_cit.bp)
    app.register_blueprint(todo2_cons.bp)
    app.register_blueprint(todo2_pago.bp)
    app.register_blueprint(todo2_encuesta.bp)


    app.register_blueprint(todo3.bp)
    app.register_blueprint(todo3_cita.bp)
    app.register_blueprint(todo3_encuesta.bp)
    app.register_blueprint(todo3_cons.bp)

    @app.route('/')
    def hola():
        return render_template('authless/indexs.html')
    return app