class Vehiculo:
    def __init__(self, venta, vendedor, marca, modelo, color, año):
        self.venta = venta
        self.vendedor = vendedor
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
    def mostrar_info(self):
        print(f"""Características:
        Venta: {self.venta}
        Concesionario: {self.vendedor}
        Marca: {self.marca}
        Modelo: {self.modelo}
        Color: {self.color}
        Año: {self.año}""")
def registrar_vehiculo():
    venta = input("Ingrese si el vehículo fue vendido o no: ")
    vendedor = input("Ingrese el nombre del concesionario: ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    color = input("Ingrese el color del vehículo: ")
    año = int(input("Ingrese el año del vehículo: "))
    return Vehiculo(venta, vendedor, marca, modelo, color, año)

menu = """Menu:
1. Registrar venta Vehículo
2. Salir"""
vehiculo1 = None
opcion = None
while opcion != 2:
    print(menu)
    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        vehiculo1 = registrar_vehiculo()
        vehiculo1.mostrar_info()
    elif opcion == 2:
        print("Chao!!")
    else:
        print("Opción no disponible")

