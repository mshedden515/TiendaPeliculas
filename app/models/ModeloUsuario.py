
from .entities.Usuario import Usuario
from .entities.Tipousuario import TipoUsuario

class ModeloUsuario():

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT id, usuario, password 
                    FROM usuario WHERE usuario = '{0}'""".format(usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                coincide = Usuario.verificar_password(data[2],usuario.password) #Chequea el pass de la DB contra el pass ingresado en Login
                if coincide:
                    usuario_logueado = Usuario(data[0],data[1],None,None)
                    return usuario_logueado
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT USU.id, USU.usuario, TIP.id, TIP.nombre
                    FROM usuario USU JOIN tipousuario TIP ON USU.tipousuario_id = TIP.id
                    WHERE USU.id = {0}""".format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            tipousuario = TipoUsuario(data[2], data[3])
            usuario_logueado = Usuario(data[0], data[1], None, tipousuario)
            return usuario_logueado
        except Exception as ex:
            raise Exception(ex)