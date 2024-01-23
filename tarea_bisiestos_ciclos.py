year = input("Introduce un año entre 1900 y 2199: ")
if  year.isdecimal() and (1900 <= int(year) <=2199):
    year = int(year)
    if year%4 == 0:
        if year%100 == 0 and year%400 != 0:
            print(f"{year} no es un año biciesto")
        else:
            print(f"{year} es un año biciesto")
    else:
       print(f"{year} no es un año biciesto")
    nro_anos_bisiestos = 0
    for año in range(1904, year +1, 4):
       nro_anos_bisiestos += 1
    if year >= 2100:
        print(f"Entre 1900 y {year} hay {nro_anos_bisiestos - 1} años bisiestos")
    else:
        print(f"Entre 1900 y {year} hay {nro_anos_bisiestos} años bisiestos")
else: 
    print(f"El valor {year} es invalido, debes escoger un numero entre 1900 y 2199")