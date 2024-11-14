""" 
    3. Imprime en pantalla, solo usando un bucle, todos los números del 0 al 99 excepto el 3, el 6 y el 11.


    @author Victor Fernandez España

"""

numerosBaneados = [3, 6, 11]
for i in range(100):
    if i not in numerosBaneados:
        print(f" {i} ")
