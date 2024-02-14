class Carro:
    def __init__(self, marca, ano, modelo, tipo, color, transmision):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.tipo = tipo
        self.color = color
        self.transmision = transmision
    def mostrar_informacion(self):
        return print(f"""Carro: 
    Marca: {self.marca} 
    Modelo: {self.modelo} 
    Año: {self.ano} 
    Tipo: {self.tipo} 
    Color: {self.color} 
    Transmision: {self.transmision}""")

class Barco: 
    def __init__(self, marca, ano, color, dimensiones, capacidad):
        self.marca = marca
        self.ano = ano
        self.color = color
        self.dimensiones = dimensiones
        self.capacidad = capacidad
    def mostrar_informacion(self):
        return print(f"""Barco: 
    Marca: {self.marca} 
    Año: {self.ano} 
    Color: {self.color} 
    Dimensiones: {self.dimensiones} 
    Capacidad: {self.capacidad} personas""")

class Avion: 
    def __init__(self, marca, ano, color, tipo, capacidad, motor):
        self.marca = marca
        self.ano = ano
        self.color = color
        self.tipo = tipo
        self.capacidad = capacidad
        self.motor = motor
    def mostrar_informacion(self):
        return print(f"""Avion: 
    Marca: {self.marca} 
    Año: {self.ano} 
    Color: {self.color} 
    Tipo: {self.tipo} 
    Capacidad: {self.capacidad} personas
    Motor: {self.motor}""")

vehiculo1 = Carro("Audi", 2019, "R8", "Deportivo", "Blanco", "Manual")
vehiculo1.mostrar_informacion()
vehiculo2 = Barco("Lamborghini", 2023, "Dorado y negro", "8mx16m", 16)
vehiculo2.mostrar_informacion()
vehiculo3 = Avion("Boeing", 2000, "Blanco", "Comercial", 190, "Pratt & Whitney JT8D")
vehiculo3.mostrar_informacion()
vehiculo4 = Carro("Porsche", 2016, "Cayenne", "SUV", "Arena", "Automatica")
vehiculo4.mostrar_informacion()
vehiculo5 = Barco("Bavaria", 2010, "Blanco", "19mx30m", 58)
vehiculo5.mostrar_informacion()
vehiculo6 = Avion("Citation", 2021, "Negro", "Privado", 20, "Cessna Citation X+")
vehiculo6.mostrar_informacion()



