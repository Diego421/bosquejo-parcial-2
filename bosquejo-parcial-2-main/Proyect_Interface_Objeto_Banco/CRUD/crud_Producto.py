


from Modelo.Producto import Productos

productos = []

def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    producto = Productos(nombre, precio)
    productos.append(producto)
    print(f"Producto {nombre} creado con éxito.")

def Listar_productos():
    if not productos:
        print("No hay productos registrados.")
    for producto in productos:
        print(producto)

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto.nombre == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado.")
            return
    print("Producto no encontrado.")