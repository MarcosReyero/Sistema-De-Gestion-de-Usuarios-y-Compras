# Sistema de Gestión de Usuarios y Compras en Línea

## Descripción

Este proyecto es una extensión del gestor de usuarios creado en la primera pre-entrega. La segunda pre-entrega amplía las funcionalidades originales para incluir un sistema completo de comercio electrónico. Ahora, el sistema no solo gestiona usuarios, sino que también permite a los usuarios comprar productos y gestionar su carrito de compras.

## Funcionalidades

### Gestión de Usuarios

- Registro de nuevos usuarios con validación de longitud para nombre de usuario y contraseña.
- Inicio de sesión y autenticación con hash de contraseñas.
- Personalización del perfil de usuario, incluyendo cambio de nombre de usuario y contraseña.

### Sistema de Compras

- Visualización de productos disponibles.
- Compra de productos y gestión del carrito de compras.
- Visualización del contenido del carrito y seguimiento de las compras realizadas.

## Estructura del Proyecto

- `gestor_de_usuarios/`

  - `__init__.py` - Inicialización del módulo.
  
  - `utils.py` - Funciones utilitarias como manejo de entrada del usuario y limpieza de pantalla.
  - `autenticacion.py` - Funciones relacionadas con la autenticación de usuarios.
  - `perfil.py` - Funciones para la personalización del perfil de usuario.
  - `ventas.py` - Funciones para manejar productos y el carrito de compras.
- `main.py` - Archivo principal que ejecuta el sistema, mostrando menús y manejando la lógica de flujo.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git

2. Navega al directorio del proyecto

    ```bash
    cd tu-repositorio

Asegúrate de tener Python 3.10 o superior instalado en tu sistema.

3. Ejecuta el programa:

python main.py

## Uso

Al iniciar el programa, se presenta un menú principal donde los usuarios pueden:

Iniciar sesión o registrarse.
Personalizar su perfil.
Comprar productos y gestionar el carrito de compras.
Cerrar sesión o salir del programa.
Durante la ejecución, puedes navegar por el menú y realizar las diferentes acciones disponibles.

Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor sigue estos pasos:

### . Haz un fork del repositorio.

### . Crea una nueva rama para tu característica o corrección:

## git checkout -b mi-nueva-caracteristica
Realiza tus cambios y haz un commit:


git add .
git commit -m "Añadida nueva característica"
Sube tus cambios:


git push origin mi-nueva-caracteristica
Crea un Pull Request en GitHub.


Contacto
Para cualquier pregunta o comentario, puedes contactarme a través de reyeromateo@gmail.com