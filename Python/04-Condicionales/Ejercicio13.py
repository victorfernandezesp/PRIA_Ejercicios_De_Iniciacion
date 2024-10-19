""" 
    13. Dado cinco enteros, devuelve verdadero si aparece alguna vez 3 enteros impares consecutivos.



    @author Victor Fernandez España

"""

entero1 = int(input("Introduce un número:       "))
entero2 = int(input("Introduce un número:       "))
entero3 = int(input("Introduce un número:       "))
entero4 = int(input("Introduce un número:       "))
entero5 = int(input("Introduce un número:       "))

esImPar1 = entero1%2==1
esImPar2 = entero2%2==1
esImPar3 = entero3%2==1
esImPar4 = entero4%2==1
esImPar5 = entero5%2==1

if esImPar1 and esImPar2 and esImPar3:
    print(f"True")
elif esImPar2 and esImPar3 and esImPar4:
    print(f"True")
elif esImPar3 and esImPar4 and esImPar5:
    print(f"True")
else:
    print(f"False")
