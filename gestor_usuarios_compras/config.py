import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Crear el directorio data si no existe
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Rutas para los archivos JSON
USER_DATA_FILE = os.path.join(DATA_DIR, 'usuarios.json')
PRODUCT_DATA_FILE = os.path.join(DATA_DIR, 'productos.json')
