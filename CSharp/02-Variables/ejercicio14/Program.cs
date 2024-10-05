
using System;

/* 
    14. Concatena dos números, convierte el resultado a entero y súmale 5.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        // Sin pasar como parámetros
        string numero1 = "2";
        string numero2 = "4";
        string concatenado1 = numero1 + numero2;
        Console.WriteLine("Concatenado: " + concatenado1);
        Console.WriteLine("Concatenado, pasadolo a entero y sumando 5: " + (Convert.ToInt32(concatenado1) + 5));

        string numero3 = "1";
        string numero4 = "6";
        string concatenado2 = numero1 + numero2;

        Console.WriteLine("Concatenado: " + concatenado2);
        Console.WriteLine("Concatenado, pasadolo a entero y sumando 5: " + (Convert.ToInt32(concatenado2) + 5));

        string numero5 = "8";
        string numero6 = "1";
        string concatenado3 = numero1 + numero2;

        Console.WriteLine("Concatenado: " + concatenado3);
        Console.WriteLine("Concatenado, pasadolo a entero y sumando 5: " + (Convert.ToInt32(concatenado3) + 5));


        // Pasando como parámetros
        Console.WriteLine("Escribe el número 1");
        string input1 = Console.ReadLine() ?? "0";
        double numeroA = Convert.ToSingle(input1);

        Console.WriteLine("Escribe el número 2");
        string input2 = Console.ReadLine() ?? "0";
        double numeroB = Convert.ToSingle(input2);


        string concatenado4 = numeroA + numeroB;

        Console.WriteLine("Concatenado: " + concatenado4);
        Console.WriteLine("Concatenado, pasadolo a entero y sumando 5: " + (Convert.ToInt32(concatenado4) + 5));

    }
}
