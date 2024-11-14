""" 
    5. Suma todos los dígitos de un número dado.


    @author Victor Fernandez España

"""

nuemerodado = 97789
nuemerodado = str(nuemerodado)
acumulador = 0
for i in (nuemerodado):
    acumulador += int(i)
print(acumulador)