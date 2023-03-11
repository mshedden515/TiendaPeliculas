from werkzeug.security import check_password_hash
from flask_login import UserMixin #UserMixin es el gestionador de sesiones

class Usuario(UserMixin):

    def __init__(self, id, usuario, password, tipousuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipousuario = tipousuario

    #En encriptado genero el pass, coincide compara ese hash con el texto plano, si coinciden devuelve True
    @classmethod
    def verificar_password(self, encriptado, password):
        #encriptado = generate_password_hash(password)
        return check_password_hash(encriptado, password)
         