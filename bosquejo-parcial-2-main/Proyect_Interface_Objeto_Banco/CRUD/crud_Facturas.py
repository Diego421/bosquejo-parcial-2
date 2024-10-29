

from CRUD.crud_Producto import Listar_productos
from Modelo.Factura import Factura
from CRUD.crud_Cliente import clientes
from CRUD.crud_Producto import productos

facturas = []

def crear_factura():
    cedula_cliente = input("Ingrese la cédula del cliente: ")
    cliente = next((c for c in clientes if c.cedula == cedula_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return

    fecha = input("Ingrese la fecha de la factura (YYYY-MM-DD): ")
    factura = Factura(cliente, fecha)

    while True:
        Listar_productos()
        nombre_producto = input("Ingrese el nombre del producto a agregar (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break

        producto = next((p for p in productos if p.nombre == nombre_producto), None)
        if producto:
            factura.agregar_producto(producto)
        else:
            print("Producto no encontrado.")

    facturas.append(factura)
    cliente.agregar_pedido(factura)
    print("Factura creada con éxito.")

def listar_facturas():
    if not facturas:
        print("No hay facturas registradas.")
    for factura in facturas:
        print(factura)