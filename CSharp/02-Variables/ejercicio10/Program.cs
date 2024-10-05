
using System;

/* 
    10. Inicializa una variable fahrenheit, calcula su equivalente a grados Celsius e ímprimelo por pantalla. Fórmula: celsius = (fahrenheit - 32) / 1.8.


    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        double fahrenheit = 91.4;
        double celsius = (fahrenheit - 32) / 1.8;
        Console.WriteLine("Grados Celsius:   " + celsius);

    }
}
