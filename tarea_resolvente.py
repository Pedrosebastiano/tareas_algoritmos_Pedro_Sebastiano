import math
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
c = input("Ingrese el valor de c: ")
a, b, c = float(a), float(b), float(c)
if (b**2 - 4*a*c) > 0:
    x1 = round(((-b) + math.sqrt(b**2 - (4*a*c))) / 2*a, 2)
    x2 = round(((-b) - math.sqrt(b**2 - (4*a*c))) / 2*a, 2)
    print(f"La ecuaciion tiene 2 soluciones, el valor de X1 = {x1} y de X2 = {x2}")
elif (b**2 - 4*a*c) == 0:
    x1 = round(((-b) + math.sqrt(b**2 - (4*a*c))) / 2*a, 2)
    print(f"La ecuaciion tiene 1 solucion, el valor de X1 = {x1}")
else:
    print(f"La ecuacion no tiene soluciones en los reales")