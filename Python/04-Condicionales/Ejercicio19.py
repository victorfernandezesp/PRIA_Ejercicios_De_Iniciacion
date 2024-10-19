""" 
    19. Determina en una partida finalizada de tres en raya si gana O, gana X o hay empate.


    @author Victor Fernandez España

"""

tablero = [
    [
        input("Introduce (X/O) "),
        input("Introduce (X/O) "),
        input("Introduce (X/O) "),
    ],
    [
        input("Introduce (X/O) "),
        input("Introduce (X/O) "),
        input("Introduce (X/O) "),
    ],
    [
        input("Introduce (X/O) "),
        input("Introduce (X/O) "),
        input("Introduce (X/O) "),
    ],
]


if tablero[0][0] == tablero[0][1] == tablero[0][2] and tablero[0][0] != "":
    ganador = tablero[0][0]
elif tablero[1][0] == tablero[1][1] == tablero[1][2] and tablero[1][0] != "":
    ganador = tablero[1][0]
elif tablero[2][0] == tablero[2][1] == tablero[2][2] and tablero[2][0] != "":
    ganador = tablero[2][0]


elif tablero[0][0] == tablero[1][0] == tablero[2][0] and tablero[0][0] != "":
    ganador = tablero[0][0]
elif tablero[0][1] == tablero[1][1] == tablero[2][1] and tablero[0][1] != "":
    ganador = tablero[0][1]
elif tablero[0][2] == tablero[1][2] == tablero[2][2] and tablero[0][2] != "":
    ganador = tablero[0][2]


elif tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "":
    ganador = tablero[0][0]
elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "":
    ganador = tablero[0][2]
else:
    ganador = "Empate"

# Resultado
if ganador == "Empate":
    print("Empate.")
else:
    print(f"Ha ganado: {ganador}")
