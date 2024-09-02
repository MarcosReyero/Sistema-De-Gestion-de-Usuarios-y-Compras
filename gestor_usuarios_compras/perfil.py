from gestor_usuarios_compras.utils import solicitar_entrada, mostrar_mensaje_y_pausar, hash_password, escribir_datos, verify_password
from gestor_usuarios_compras.usuarios import cargar_usuarios, verificar_usuario_existe

def personalizar_perfil():
    print("\n### PERSONALIZAR PERFIL ###\n")
    usuario_actual = solicitar_entrada("Usuario actual: ", 3, 20)
    password_actual = solicitar_entrada("Contraseña actual: ", 8, 20)

    if not usuario_actual or not password_actual:
        mostrar_mensaje_y_pausar("\nUsuario o contraseña no pueden estar vacíos.")
        return

    datos = cargar_usuarios()  
    usuarios = datos.get("usuarios", []) 

    usuario_valido = False
    usuario_a_actualizar = None

    for dict_usuario in usuarios:
       
        stored_hash = dict_usuario["password"]
        stored_salt = dict_usuario["salt"]
        if usuario_actual == dict_usuario["usuario"] and verify_password(password_actual, stored_hash, stored_salt):
            usuario_valido = True
            usuario_a_actualizar = dict_usuario
            break

    if not usuario_valido:
        mostrar_mensaje_y_pausar("\nUsuario o contraseña incorrectos.")
        return

    nuevo_usuario = solicitar_entrada("Nuevo usuario: ", 3, 20)

    if verificar_usuario_existe(nuevo_usuario):
        mostrar_mensaje_y_pausar("\nEl nuevo nombre de usuario ya está registrado. Intenta con otro.")
        return

    nuevo_password = solicitar_entrada("Nueva contraseña: ", 8, 20)
    nuevo_password_hashed, nuevo_salt = hash_password(nuevo_password)
    
    if usuario_a_actualizar:
        usuario_a_actualizar["usuario"] = nuevo_usuario
        
        if isinstance(nuevo_password_hashed, bytes):
            usuario_a_actualizar["password"] = nuevo_password_hashed.hex()
        else:
            usuario_a_actualizar["password"] = nuevo_password_hashed
        
        usuario_a_actualizar["salt"] = nuevo_salt.hex()

        usuarios = [u for u in usuarios if u["usuario"] != usuario_actual]
        usuarios.append(usuario_a_actualizar)
        escribir_datos("gestor_usuarios_compras/data/usuarios.json", {"usuarios": usuarios})

    mostrar_mensaje_y_pausar("\nPerfil actualizado exitosamente.")
