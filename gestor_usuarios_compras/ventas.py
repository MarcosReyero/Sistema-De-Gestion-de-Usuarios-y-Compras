from .utils import input_con_control, mostrar_mensaje_y_pausar

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto):
        self.items.append(producto)

    def mostrar_carrito(self):
        if not self.items:
            print("\nEl carrito está vacío.")
        else:
            print("\n### CARRITO DE COMPRAS ###\n")
            total = 0
            for i, producto in enumerate(self.items, start=1):
                print(f"{i}) {producto.nombre} - ${producto.precio:.2f}")
                total += producto.precio
            print(f"\nTotal: ${total:.2f}")

productos_disponibles = [
    Producto("Producto 1", 50.00),
    Producto("Producto 2", 75.00),
    Producto("Producto 3", 100.00)
]

def comprar_producto(carrito):
    """
    Permite al usuario seleccionar un producto y añadirlo al carrito.

    Parámetros:
    carrito (Carrito): El carrito al que se añadirá el producto.
    """
    print("\n### PRODUCTOS DISPONIBLES ###\n")
    for i, producto in enumerate(productos_disponibles, start=1):
        print(f"{i}) {producto.nombre} - ${producto.precio:.2f}")

    opcion = input_con_control("\nSelecciona el número del producto que deseas comprar: ")
    if opcion.isdigit() and 1 <= int(opcion) <= len(productos_disponibles):
        producto_seleccionado = productos_disponibles[int(opcion) - 1]
        carrito.agregar_producto(producto_seleccionado)
        mostrar_mensaje_y_pausar(f"\n{producto_seleccionado.nombre} añadido al carrito.")
    else:
        mostrar_mensaje_y_pausar("\nOpción inválida. Por favor, selecciona un producto válido.")
