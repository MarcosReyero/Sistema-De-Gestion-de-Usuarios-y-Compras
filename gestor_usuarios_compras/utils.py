import os
import hashlib

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
    try:
        return hashlib.sha256(password.encode()).hexdigest()
    except Exception as e:
        print(f"Error al generar hash de la contraseña: {e}")
        return ""

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
