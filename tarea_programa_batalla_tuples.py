import random
def malicioso(PS, PD):
    return (PS - ataques["1"][0], PD - ataques["1"][1])
def placaje(PS, PD):
    return (PS - ataques["2"][0], PD - ataques["2"][1])
def ascuas(PS, PD):
    return (PS - ataques["3"][0], PD -ataques["3"][1])
def latigo(PS, PD):
    return (PS - ataques["1"][0], PD - ataques["1"][1])


jugador_sal_def = (100,100)
oponente_sal_def = (100,100)
jugadas = ["malicioso", "placaje", "ascuas"]
while jugador_sal_def[0] > 0 and oponente_sal_def[0] > 0:
    ataque_jugador = input("Ingrese un ataque: ").lower()
    ataques = {"1" : (0 , 10), "2": ((35/ (oponente_sal_def[1]/100)), 0) , "3" : (20, 0)}
    if ataque_jugador == jugadas[0]:
        oponente_sal_def = malicioso(oponente_sal_def[0], oponente_sal_def[1])
        if oponente_sal_def[1] <= 0:
            oponente_sal_def = (oponente_sal_def[0], 1)
    elif ataque_jugador == jugadas[1]:
        oponente_sal_def = placaje(oponente_sal_def[0], oponente_sal_def[1])
    elif ataque_jugador == jugadas[2]: 
        oponente_sal_def = ascuas(oponente_sal_def[0], oponente_sal_def[1])
    else: 
        print(f"Ese ataque no es valido. Tus ataque son {jugadas} ")
        continue   
#TURNO OPONENTE
    ataques = {"1" : (10 , 10), "2": ((35/ (jugador_sal_def[1]/100)), 0) , "3" : (40, 0)}
    ataque_oponente = random.randrange (1, 4)
    if ataque_oponente == 1:
        jugador_sal_def = latigo(jugador_sal_def[0], jugador_sal_def[1] )
        if jugador_sal_def[1] <= 0:
            jugador_sal_def = (jugador_sal_def[0], 1)
    elif ataque_oponente == 2:
        jugador_sal_def = placaje(jugador_sal_def[0], jugador_sal_def[1])
    elif ataque_oponente == 3: 
        jugador_sal_def = ascuas(jugador_sal_def[0], jugador_sal_def[1])
if oponente_sal_def[0] <= 0 and jugador_sal_def[0] <= 0 :
    print("Empate")
elif oponente_sal_def[0] <= 0:
    print("Felicidades haz ganado")
else:
    print("Lo siento haz perdido")