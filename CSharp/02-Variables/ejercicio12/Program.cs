
using System;

/* 
    12. Realiza un conversor de Fahrenheit a Celsius.


    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        // Sin pasar como parámetros
        double numero1 = 68;
        double numero2 = 13;
        double numero3 = -145.6;

        Console.WriteLine(numero1 + "ºF = " + (((double)5 / 9) * (numero1 - 32)) + "ºC");
        Console.WriteLine(numero2 + "ºF = " + (((double)5 / 9) * (numero2 - 32)) + "ºC");
        Console.WriteLine(numero3 + "ºF = " + (((double)5 / 9) * (numero3 - 32)) + "ºC");


        // Pasando como parámetros
        Console.WriteLine("Escribe el número 1");
        string input1 = Console.ReadLine() ?? "0";
        double numeroA = Convert.ToSingle(input1);


        Console.WriteLine(numeroA + "ºF = " + (((double)5 / 9) * (numeroA - 32)) + "ºC");

    }
}
