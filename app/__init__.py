from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from .models.ModeloLibro import ModeloLibro
from .models.entities.Usuario import Usuario
from .models.ModeloUsuario import ModeloUsuario
from flask_login import LoginManager, login_user, logout_user

app = Flask(__name__)

csrf = CSRFProtect() #Proteccion contra el acceso irrestricto, genera token de usuario para cada sesion
db = MySQL(app)
login_manager_app = LoginManager(app)

""" Esta funcionalidad debe estar implementada para el correcto manejo de las sesiones a traves de Flask_Login
user_loader es un metodo que se va a ejecutar cada vez que hagamos referencia a la sesion del usuario
"""
@login_manager_app.user_loader 
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(None, request.form['usuario'], request.form['password'], None)
        usuario_logueado = ModeloUsuario.login(db, usuario)
        if (usuario_logueado != None):
            login_user(usuario_logueado)
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/libros') #En data obtengo el resultado de la consulta y lo paso a la vista
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        print(ex)


def pagina_no_encontrada(error):
    return render_template('/errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
