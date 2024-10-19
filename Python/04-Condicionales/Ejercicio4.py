""" 
    4. Crear un programa que determine si un número es menor que 0, o que está entre 0 y 50, o entre 51 y 100 o por encima de 100.



    @author Victor Fernandez España

"""

a = 56

if a < 0:
    print(f"Es menor que 0")
elif 0 <= a <= 50:
    print(f"Está entre 0 y 50")
elif 51 <= a <= 100:
    print(f"Está entre 51 y 100")

else:
    print(f"Es mamyor a 100")
