

from CRUD.crud_Cliente import crear_cliente, listar_clientes, eliminar_cliente
from CRUD.crud_Producto import crear_producto, Listar_productos, eliminar_producto
from CRUD.crud_Facturas import crear_factura, listar_facturas

def mostrar_menu():
    print("\n--- Sistema de Facturación ---")
    print("1. Crear Cliente")
    print("2. Listar Clientes")
    print("3. Eliminar Cliente")
    print("4. Crear Producto")
    print("5. Listar Productos")
    print("6. Eliminar Producto")
    print("7. Crear Factura")
    print("8. Listar Facturas")
    print("0. Salir")

def ejecutar_opcion(opcion):
    if opcion == '1':
        crear_cliente()
    elif opcion == '2':
        listar_clientes()
    elif opcion == '3':
        eliminar_cliente()
    elif opcion == '4':
        crear_producto()
    elif opcion == '5':
        Listar_productos()
    elif opcion == '6':
        eliminar_producto()
    elif opcion == '7':
        crear_factura()
    elif opcion == '8':
        listar_facturas()
    elif opcion == '0':
        print("Saliendo del sistema...")
    else:
        print("Opción no válida")

def iniciar_sistema():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        ejecutar_opcion(opcion)
        if opcion == '0':
            break