

from Modelo.Cliente import Cliente

clientes = []

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cédula del cliente: ")
    cliente = Cliente(nombre, cedula)
    clientes.append(cliente)
    print(f"Cliente {nombre} creado con éxito.")

def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
    for cliente in clientes:
        print(cliente)

def eliminar_cliente():
    cedula = input("Ingrese la cédula del cliente a eliminar: ")
    for cliente in clientes:
        if cliente.cedula == cedula:
            clientes.remove(cliente)
            print(f"Cliente con cédula {cedula} eliminado.")
            return
    print("Cliente no encontrado.")