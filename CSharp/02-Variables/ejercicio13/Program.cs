
using System;

/* 
    13. Calcula el área y el perímetro de un rectángulo dado sus lados.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        // Sin pasar como parámetros
        double numero1 = 3;
        double numero2 = 2;

        Console.WriteLine("Área: " + (numero1 * numero2));
        Console.WriteLine("Perímetro: " + ((numero1 * 2) + (numero2 * 2)));

        double numero3 = 2;
        double numero4 = 4;

        Console.WriteLine("Área: " + (numero3 * numero4));
        Console.WriteLine("Perímetro: " + ((numero3 * 2) + (numero4 * 2)));

        double numero5 = 4;
        double numero6 = 5;

        Console.WriteLine("Área: " + (numero5 * numero6));
        Console.WriteLine("Perímetro: " + ((numero5 * 2) + (numero6 * 2)));



        // Pasando como parámetros
        Console.WriteLine("Escribe el número 1");
        string input1 = Console.ReadLine() ?? "0";
        double numeroA = Convert.ToSingle(input1);

        Console.WriteLine("Escribe el número 2");
        string input2 = Console.ReadLine() ?? "0";
        double numeroB = Convert.ToSingle(input2);


        Console.WriteLine("Área: " + (numeroA * numeroB));
        Console.WriteLine("Perímetro: " + ((numeroA * 2) + (numeroB * 2)));

    }
}
