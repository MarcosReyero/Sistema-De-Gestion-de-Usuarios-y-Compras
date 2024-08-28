from gestor_de_usuarios.utils import hash_password

usuarios_registrados = []

def verificar_usuario_existe(usuario):
    for dict_usuario in usuarios_registrados:
        if usuario == dict_usuario["usuario"]:
            return True
    return False

def agregar_usuario(usuario, password):
    password_hashed = hash_password(password)
    dict_usuario = {"usuario": usuario, "password": password_hashed}
    usuarios_registrados.append(dict_usuario)
