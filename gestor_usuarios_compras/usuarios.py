import os,json
from gestor_usuarios_compras.utils import leer_datos, escribir_datos,verify_password
from .config import USER_DATA_FILE

archivo_usuarios = "gestor_usuarios_compras/data/usuarios.json"

def verificar_usuario_existe(usuario):
    """Verifica si un usuario ya existe en el archivo JSON."""
    datos = leer_datos(archivo_usuarios)
    usuarios = datos.get("usuarios", [])
    return any(usuario == u["usuario"] for u in usuarios)

def verificar_usuario_y_password(usuario, password):
    """Verifica si el usuario y la contraseña son correctos."""
    datos = leer_datos(archivo_usuarios)
    usuarios = datos.get("usuarios", [])
    for dict_usuario in usuarios:
        if usuario == dict_usuario["usuario"]:
            return verify_password(
                bytes.fromhex(dict_usuario["password"]),
                bytes.fromhex(dict_usuario["salt"]),
                password
            )
    return False

def agregar_usuario(usuario, password_hash, salt):
    """Agrega un nuevo usuario al archivo JSON."""
    datos = leer_datos(USER_DATA_FILE)
    if "usuarios" not in datos:
        datos["usuarios"] = []
    datos["usuarios"].append({
        "usuario": usuario,
        "password": password_hash,
        "salt": salt
    })
    escribir_datos(USER_DATA_FILE, datos)

def cargar_usuarios():
    """Cargar la lista de usuarios desde el archivo JSON."""
    datos = leer_datos(USER_DATA_FILE)
    return datos 