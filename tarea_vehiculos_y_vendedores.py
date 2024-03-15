class Seller:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Vehicle:
    def __init__(self, color, marca, ano, capacidad):
        self.color = color 
        self.marca = marca
        self.ano = ano
        self.capacidad = capacidad
        self.seller = None
    
    def set_seller(self, seller):
        self.seller = seller
    
    def mostrar_informacion(self):
        print(f"""Vehiculo:
    Color: {self.color} 
    Marca: {self.marca} 
    Año: {self.ano} 
    Capacidad: {self.capacidad}
    """)
        if self.seller:
            print(f"Concesionario: {self.seller.name}, Ubicación: {self.seller.location}")

def registrar_vehiculo():
    color = input("Ingrese el color del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    ano = int(input("Ingrese el año del vehículo: "))
    capacidad = int(input("Ingrese la capacidad del vehículo: "))
    return Vehicle(color, marca, ano, capacidad)

def main():
    sellers = [Seller("REX Cars", "Av. Francisco de Miranda"), Seller("Altana C.A.", "Calle Londres")]
    vehicles = []
    menu = """Menu
    1. Registrar nuevo vehículo
    2. Mostrar información de vehículos
    3. Salir"""
    while True:
        print(menu)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            vehicle = registrar_vehiculo()
            print("Concesionario para el vehículo:")
            for i, seller in enumerate(sellers, 1):
                print(f"{i}. {seller.name}, {seller.location}")
            seller_index = int(input("Ingrese el número correspondiente al concesionario: ")) - 1
            vehicle.set_seller(sellers[seller_index])
            vehicles.append(vehicle)
            print("Vehículo registrado exitosamente.")
        elif opcion == "2":
            if not vehicles:
                print("No hay vehículos registrados.")
            else:
                print("Información de vehículos:")
                for vehicle in vehicles:
                    vehicle.mostrar_informacion()
        elif opcion == "3":
            print("Chao!!!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


main()