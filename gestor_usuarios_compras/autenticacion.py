from gestor_usuarios_compras.utils import mostrar_mensaje_y_pausar, hash_password, solicitar_entrada
from gestor_usuarios_compras.usuarios import usuarios_registrados, verificar_usuario_existe, agregar_usuario

def iniciar_sesion():
    print("\n### INICIAR SESIÓN ###\n")
    usuario = solicitar_entrada("Usuario: ", 3, 20)
    password = solicitar_entrada("Contraseña: ", 8, 20)

    if not usuario or not password:
        mostrar_mensaje_y_pausar("\nUsuario o contraseña no pueden estar vacíos.")
        return False

    password_hashed = hash_password(password)

    for dict_usuario in usuarios_registrados:
        if usuario == dict_usuario["usuario"] and password_hashed == dict_usuario["password"]:
            mostrar_mensaje_y_pausar("\n¡Has iniciado sesión con éxito!")
            return True

    mostrar_mensaje_y_pausar("\nUsuario o contraseña incorrectos.")
    return False

def registrar_usuario():
    print("\n### REGISTRARSE ###")
    mostrar_requisitos()
    usuario = solicitar_entrada("Usuario: ", 3, 20)

    if verificar_usuario_existe(usuario):
        mostrar_mensaje_y_pausar("\nEl nombre de usuario ya está registrado. Intenta con otro.")
        return

    password = solicitar_entrada("Contraseña: ", 8, 20)
    agregar_usuario(usuario, password)
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
