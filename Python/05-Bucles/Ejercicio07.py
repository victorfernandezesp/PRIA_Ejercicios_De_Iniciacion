""" 
    7. Imprime en pantalla todos los números primos desde el 2, incluído, hasta un entero dado.

    @author Victor Fernandez España

"""

nuemerodado = 10
if nuemerodado == 1:
    print(f"Es un numero primo.")
else:
    for j in range(2, nuemerodado+1):
        primo = True
        for i in range(2, int(j**0.5) + 1):
            if j % i == 0:
                primo = False
                break
        if primo:
            print(f"{j} es PRIMO.")
