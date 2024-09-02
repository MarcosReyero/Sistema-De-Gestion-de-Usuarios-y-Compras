from gestor_usuarios_compras.utils import (
    mostrar_mensaje_y_pausar, 
    hash_password, 
    solicitar_entrada, 
    verify_password,
    escribir_datos,
)
from .config import USER_DATA_FILE
from .usuarios import cargar_usuarios, verificar_usuario_existe


def iniciar_sesion():
    """Permite a un usuario iniciar sesión proporcionando nombre de usuario y contraseña."""
    print("\n### INICIAR SESIÓN ###")
    usuario = solicitar_entrada("Usuario: ", 3, 20)
    contraseña = solicitar_entrada("Contraseña: ", 8, 20)
    
    usuarios_registrados = cargar_usuarios()
    
    if "usuarios" not in usuarios_registrados:
        mostrar_mensaje_y_pausar("No se encontraron usuarios registrados.")
        return False
    
    for u in usuarios_registrados["usuarios"]:
        if isinstance(u, dict) and u.get("usuario") == usuario:
            if verify_password(contraseña, u.get("password"), u.get("salt")):
                mostrar_mensaje_y_pausar("Inicio de sesión exitoso.")
                return True
            else:
                mostrar_mensaje_y_pausar("Contraseña incorrecta.")
                return False
    
    mostrar_mensaje_y_pausar("Usuario no encontrado.")
    return False

def registrar_usuario():
    print("\n### REGISTRARSE ###")
    mostrar_requisitos()
    usuario = solicitar_entrada("Usuario: ", 3, 20)

    if verificar_usuario_existe(usuario):
        mostrar_mensaje_y_pausar("\nEl nombre de usuario ya está registrado. Intenta con otro.")
        return

    password = solicitar_entrada("Contraseña: ", 8, 20)
    hashed, salt = hash_password(password)
    
    # Cargar usuarios desde el archivo
    usuarios_registrados = cargar_usuarios()
    
    if "usuarios" not in usuarios_registrados:
        usuarios_registrados["usuarios"] = []
        
    nuevo_usuario = {
        "usuario": usuario,
        "password": hashed.hex(),
        "salt": salt.hex()
    }
    
    # Depuración: Imprimir el contenido antes de guardar
    # print(f"Usuarios Registrados: {usuarios_registrados}")
    # print(f"Nuevo Usuario: {nuevo_usuario}")
    
    usuarios_registrados["usuarios"].append(nuevo_usuario)
    
    # Guardar usuarios en el archivo JSON
    escribir_datos(USER_DATA_FILE, usuarios_registrados)

    mostrar_mensaje_y_pausar("\nTe has registrado exitosamente.")

def mostrar_requisitos():
    requisitos_usuario = (
        "Requisitos para el nombre de usuario:\n"
        "- Longitud: 3 a 20 caracteres\n"
        "- Puede incluir letras y números\n"
        "- Evitar caracteres especiales y espacios en blanco"
    )
    requisitos_password = (
        "Requisitos para la contraseña:\n"
        "- Longitud: 8 a 20 caracteres\n"
        "- Debe incluir letras (mayúsculas y minúsculas), números y caracteres especiales\n"
        "- No debe contener el nombre de usuario"
    )
    mostrar_mensaje_y_pausar(f"{requisitos_usuario}\n\n{requisitos_password}")
