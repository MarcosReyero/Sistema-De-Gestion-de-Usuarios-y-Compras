from gestor_de_usuarios.utils import solicitar_entrada, mostrar_mensaje_y_pausar, hash_password
from gestor_de_usuarios.usuarios import usuarios_registrados, verificar_usuario_existe

def personalizar_perfil():
    print("\n### PERSONALIZAR PERFIL ###\n")
    usuario_actual = solicitar_entrada("Usuario actual: ", 3, 20)
    password_actual = solicitar_entrada("Contraseña actual: ", 8, 20)

    if not usuario_actual or not password_actual:
        mostrar_mensaje_y_pausar("\nUsuario o contraseña no pueden estar vacíos.")
        return

    password_hashed = hash_password(password_actual)
    usuario_valido = False

    for dict_usuario in usuarios_registrados:
        if usuario_actual == dict_usuario["usuario"] and password_hashed == dict_usuario["password"]:
            usuario_valido = True
            break

    if not usuario_valido:
        mostrar_mensaje_y_pausar("\nUsuario o contraseña incorrectos.")
        return

    nuevo_usuario = solicitar_entrada("Nuevo usuario: ", 3, 20)

    if verificar_usuario_existe(nuevo_usuario):
        mostrar_mensaje_y_pausar("\nEl nuevo nombre de usuario ya está registrado. Intenta con otro.")
        return

    nuevo_password = solicitar_entrada("Nueva contraseña: ", 8, 20)
    nuevo_password_hashed = hash_password(nuevo_password)
    for dict_usuario in usuarios_registrados:
        if usuario_actual == dict_usuario["usuario"]:
            dict_usuario["usuario"] = nuevo_usuario
            dict_usuario["password"] = nuevo_password_hashed
            break

    mostrar_mensaje_y_pausar("\nPerfil actualizado exitosamente.")
