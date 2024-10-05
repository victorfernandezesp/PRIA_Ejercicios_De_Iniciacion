
using System;

/* 
    11. Dado tres enteros, súmalos e imprime el resultado.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        // Sin pasar como parámetros
        int numero1 = 1;
        int numero2 = 2;
        int numero3 = 3;

        Console.WriteLine(numero1 + " + " + numero2 + " + " + numero3 + " = " + (numero1 + numero2 + numero3));


        // Pasando como parámetros
        Console.WriteLine("Escribe el número 1");
        string input1 = Console.ReadLine()?? "0";
        double numeroA = Convert.ToSingle(input1);

        Console.WriteLine("Escribe el número 2");
        string input2 = Console.ReadLine()?? "0";
        double numeroB = Convert.ToSingle(input2);
        
        Console.WriteLine("Escribe el número 3");
        string input3 = Console.ReadLine()?? "0";
        double numeroC = Convert.ToSingle(input3);
        
        Console.WriteLine(numeroA + " + " + numeroB + " + " + numeroC + " = " + (numeroA + numeroB + numeroC));

    }
}
