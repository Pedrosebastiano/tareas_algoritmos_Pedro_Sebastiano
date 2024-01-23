print("Por favor coloque las cantidades de cada ingrediente para hacer arepas")
cantidad_agua = input("Ingrese cuantos tazas de agua desea colocar: ")
cantidad_harina_pan = input("Ingrese cuantas tazas de harina pan desea colocar: ")
cantidad_sal = input("Ingrese cuantos gramos de sal desea colocar: ")
cantidad_aceite = input("Ingrese mililitros de aceite desea colocar: ") 
# 1 tza = 150grs
gramos =  round(float(cantidad_aceite)+ float(cantidad_agua) * 150 + float(cantidad_harina_pan)* 150 + float(cantidad_sal) , 2)
print(f"El peso de los ingredientes de las arepas es de {gramos} grs")