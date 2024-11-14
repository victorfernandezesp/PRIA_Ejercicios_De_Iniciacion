""" 
    6. Imprime en pantalla si un entero dado es primo o no. Un número primo es un entero mayor que 1 que solo se puede dividir por 1 y por sí mismo.

    @author Victor Fernandez España

"""

nuemerodado = 6
primo = True
if nuemerodado == 1:
    print(f"Es un numero primo.")
else:
    for i in range(2, int(nuemerodado**0.5) + 1):
        if nuemerodado % i == 0:
            primo = False
            break
    if primo:
        print(f"{nuemerodado} es PRIMO.")
    else:
        print(f"{nuemerodado} NO es primo.")
