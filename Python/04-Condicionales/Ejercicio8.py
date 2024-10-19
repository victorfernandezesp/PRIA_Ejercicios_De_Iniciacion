""" 
    8. Crea un programa que encuentre el número mayor a partir de tres números dados.



    @author Victor Fernandez España

"""

numero1 = 60
numero2 = 60
numero3 = 40

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} es el mayor.")

elif numero1 < numero2 and numero2 > numero3:
    print(f"{numero2} es el mayor.")

elif numero3 > numero2 and numero1 > numero3:
    print(f"{numero3} es el mayor.")

else:
    print(f"El mayor es: {max(numero1, numero2, numero3)}")
