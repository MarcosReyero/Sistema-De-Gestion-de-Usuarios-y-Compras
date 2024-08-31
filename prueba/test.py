import sys
from gestor_usuarios_compras.utils import clear, mostrar_mensaje_y_pausar, input_con_control, confirmar_salida
from gestor_usuarios_compras.autenticacion import iniciar_sesion, registrar_usuario
from gestor_usuarios_compras.perfil import personalizar_perfil
from gestor_usuarios_compras.ventas import productos_disponibles, Carrito, comprar_producto

def main():
    carrito = Carrito()
    sesion_iniciada = False

    while True:
        try:
            clear()
            print("\n#### BIENVENIDO AL SISTEMA ####\n")
            print("1) Iniciar sesión")
            print("2) Registrarse")
            print("3) Salir")
            opcion = input_con_control("\nSelecciona una opción: ")

            if opcion == "1":
                clear()
                if iniciar_sesion():
                    sesion_iniciada = True
            elif opcion == "2":
                clear()
                registrar_usuario()
            elif opcion == "3":
                clear()
                if confirmar_salida():
                    print("¡Hasta luego!")
                    break
            else:
                clear()
                mostrar_mensaje_y_pausar("\nOpción inválida. Por favor, selecciona una opción válida.")

            while sesion_iniciada:
                try:
                    clear()
                    print("\n### MENÚ PRINCIPAL ###\n")
                    print("1) Personalizar perfil")
                    print("2) Comprar productos")
                    print("3) Ver carrito")
                    print("4) Cerrar sesión")
                    print("5) Salir")
                    opcion_menu = input_con_control("\nSelecciona una opción: ")

                    if opcion_menu == "1":
                        personalizar_perfil()
                    elif opcion_menu == "2":
                        clear()
                        comprar_producto(carrito)
                    elif opcion_menu == "3":
                        clear()
                        carrito.mostrar_carrito()
                        mostrar_mensaje_y_pausar("")
                    elif opcion_menu == "4":
                        mostrar_mensaje_y_pausar("\n¡Has cerrado sesión!")
                        sesion_iniciada = False
                    elif opcion_menu == "5":
                        if confirmar_salida():
                            print("¡Hasta luego!")
                            sesion_iniciada = False
                            break
                    else:
                        mostrar_mensaje_y_pausar("\nOpción inválida. Por favor, selecciona una opción válida.")
                
                except KeyboardInterrupt:
                    print("\n\nInterrupción detectada. Por favor, selecciona una opción válida.")

        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
