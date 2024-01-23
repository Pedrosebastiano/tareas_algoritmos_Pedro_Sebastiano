# Esta solucion pide al programa cuantos y cuales ingredientes desea colocar y sus respectivas cantidades
cantidad_ingredientes = int(input("Cuantos ingredientes desea colocar?: "))
i = 0
gramos = 0
while i < cantidad_ingredientes:
    ingrediente = input("Introduzca uno de los ingredientes: ")
    cantidad_ingrediente = float(input(f"Cuantos grs desea colocar de {ingrediente}: "))
    gramos = cantidad_ingrediente + gramos
    i += 1
print(f"El peso de los ingredientes de las arepas es de {round(gramos,2)} grs")  