
using System;

/* 
    8. Convierte una variable con identificador latitud de tipo cadena de caracteres y con valor -234.62 a tipo número real. Réstale a la variable el valor 21.34 e imprime finalmente dicha variable.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        string latitud = "-234,62";
        double valorFinal = Convert.ToSingle(latitud) - 21.34;
        Console.WriteLine("Valor final = " + valorFinal);
    }
}
