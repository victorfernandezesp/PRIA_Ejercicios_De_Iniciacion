
using System;

/* 
    15. Multiplica tres enteros, concatena el resultado con un 4 al final y divide el resultado por 2.


    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        // Sin pasar como parámetros
        int numero1 = -2;
        int numero2 = -1;
        int numero3 = 3;
        int multiplicacion1 = numero1 * numero2 * numero3;
        string concatenado1 = Convert.ToString(multiplicacion1) + "4";
        Console.WriteLine("Concatenado: " + concatenado1);
        Console.WriteLine("Concatenado, pasadolo a entero y dividiendo entre 2: " + (Convert.ToInt32(concatenado1) / 2));

        int numero4 = 3;
        int numero5 = 5;
        int numero6 = -2;
        int multiplicacion2 = numero4 * numero5 * numero6;
        string concatenado2 = Convert.ToString(multiplicacion2) + "4";
        Console.WriteLine("Concatenado: " + concatenado2);
        Console.WriteLine("Concatenado, pasadolo a entero y dividiendo entre 2: " + (Convert.ToInt32(concatenado2) / 2));


        int numero7 = 4;
        int numero8 = 3;
        int numero9 = 2;
        int multiplicacion3 = numero7 * numero8 * numero9;
        string concatenado3 = Convert.ToString(multiplicacion3) + "4";
        Console.WriteLine("Concatenado: " + concatenado3);
        Console.WriteLine("Concatenado, pasadolo a entero y dividiendo entre 2: " + (Convert.ToInt32(concatenado3) / 2));


        // Pasando como parámetros
        Console.WriteLine("Escribe el número 1");
        string input1 = Console.ReadLine() ?? "0";
        int numeroA = Convert.ToInt32(input1);

        Console.WriteLine("Escribe el número 2");
        string input2 = Console.ReadLine() ?? "0";
        int numeroB = Convert.ToInt32(input2);

        Console.WriteLine("Escribe el número 3");
        string input3 = Console.ReadLine() ?? "0";
        int numeroC = Convert.ToInt32(input3);


        int multiplicacion4 = numeroA * numeroB * numeroC;
        string concatenado4 = Convert.ToString(multiplicacion4) + "4";
        Console.WriteLine("Concatenado: " + concatenado4);
        Console.WriteLine("Concatenado, pasadolo a entero y dividiendo entre 2: " + (Convert.ToInt32(concatenado4) / 2));

    }
}
