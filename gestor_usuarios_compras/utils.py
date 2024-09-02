import os
import hashlib
import json

def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except Exception as e:
        print(f"Error al limpiar la pantalla: {e}")

def input_con_control(mensaje):
    try:
        return input(mensaje)
    except (KeyboardInterrupt, EOFError):
        return ""
    except Exception as e:
        print(f"Error al recibir entrada: {e}")
        return ""

def hash_password(password):
    """
    Hashes a password using PBKDF2 and returns the hash and salt.

    Args:
        password (str): The password to hash.

    Returns:
        tuple: A tuple containing the hashed password (bytes) and the salt (bytes).
    """
    salt = os.urandom(16)  # Genera una sal aleatoria
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_password, salt

def verify_password(password, hashed_password, salt):
    """
    Verifica la contraseña dada comparándola con el hash almacenado.

    Args:
        password (str): La contraseña proporcionada por el usuario.
        hashed_password (str or bytes): El hash de la contraseña almacenada, que puede ser una cadena hexadecimal o bytes.
        salt (str or bytes): La sal utilizada para el hash, que puede ser una cadena hexadecimal o bytes.

    Returns:
        bool: True si la contraseña es correcta, False en caso contrario.
    """
    # Convertir el hash almacenado y la sal a bytes si se pasan como cadenas hexadecimales
    if isinstance(hashed_password, str):
        hashed_password = bytes.fromhex(hashed_password)
    if isinstance(salt, str):
        salt = bytes.fromhex(salt)
    
    # Generar el hash de la contraseña proporcionada utilizando la misma sal
    new_password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    
    # Comparar el nuevo hash con el hash almacenado
    return new_password_hash == hashed_password

def mostrar_mensaje_y_pausar(mensaje):
    try:
        print(mensaje)
        input("\nPresiona Enter para continuar...")
    except Exception as e:
        print(f"Error al mostrar el mensaje: {e}")

def validar_longitud(valor, min_longitud, max_longitud):
    try:
        if len(valor) < min_longitud:
            return f"Debe tener al menos {min_longitud} caracteres."
        elif len(valor) > max_longitud:
            return f"Debe tener como máximo {max_longitud} caracteres."
        return None
    except Exception as e:
        print(f"Error al validar longitud: {e}")
        return "Error de validación"

def solicitar_entrada(mensaje, min_longitud, max_longitud):
    while True:
        valor = input_con_control(mensaje)
        error = validar_longitud(valor, min_longitud, max_longitud)
        if error:
            mostrar_mensaje_y_pausar(error)
        else:
            return valor

def confirmar_salida():
    try:
        while True:
            confirmacion = input_con_control("¿Estás seguro que deseas salir? (s/n): ").lower()
            if confirmacion in ['s', 'n']:
                return confirmacion == 's'
            else:
                mostrar_mensaje_y_pausar("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")
    except Exception as e:
        print(f"Error al confirmar salida: {e}")

def leer_datos(ruta_archivo):
    """Leer datos desde un archivo JSON, o crear el archivo con datos vacíos si no existe."""
    if not os.path.exists(ruta_archivo):
        # Crear el archivo con datos vacíos
        with open(ruta_archivo, 'w') as archivo:
            json.dump({"usuarios": []}, archivo, indent=4)
        return {"usuarios": []}

    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

def escribir_datos(ruta_archivo, datos):
    """Escribir datos en un archivo JSON."""
    with open(ruta_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def mostrar_requisitos():
    try:
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
    except Exception as e:
        print(f"Error al mostrar los requisitos: {e}")