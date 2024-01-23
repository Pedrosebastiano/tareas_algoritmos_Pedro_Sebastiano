import random
PS_oponente = 100
PS_jugador = 100
defensa_oponente = 100
defensa_jugador = 100
ataques = ["malicioso", "placaje", "ascuas"]
while PS_jugador > 0 and PS_oponente>0:
    ataque_jugador = input("Ingrese un ataque: ").lower()
    if ataque_jugador == ataques[0]:
        defensa_oponente -=10
        if defensa_oponente <= 0:
            defensa_oponente = 1
    elif ataque_jugador == ataques[1]:
        PS_oponente -= 35 / (defensa_oponente/100)
    elif ataque_jugador == ataques[2]: 
        PS_oponente -= 20
    else: 
        print(f"Ese ataque no es valido. Tus ataque son {ataques} ")
        continue   
#TURNO OPONENTE
    ataque_oponente = random.choice(ataques)
    if ataque_oponente == ataques[0]:
        defensa_jugador -= 10
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque_oponente == ataques[1]:
        PS_jugador -= 35 / (defensa_jugador/100)
    elif ataque_oponente == ataques[2]: 
        PS_jugador -= 40
if PS_oponente <= 0 and PS_jugador <= 0 :
    print("Empate")
elif PS_oponente <= 0:
    print("Felicidades haz ganado")
else:
    print("Lo siento haz perdido")
