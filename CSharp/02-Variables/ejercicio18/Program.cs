
using System;

/* 
    18. Imprime GNU si el número recibido es impar.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        // Sin pasar como parámetros
        int numero1 = 5;
        int resultado1 = (numero1 % 2);
        Console.WriteLine((resultado1 == 1) ? "GNU" : "\n");

        int numero2 = 4;
        int resultado2 = (numero2 % 2);
        Console.WriteLine((resultado2 == 1) ? "GNU" : "\n");

        
        int numero3 = 11;
        int resultado3 = (numero3 % 2);
        Console.WriteLine((resultado3 == 1) ? "GNU" : "\n");
        




        // Pasando como parámetros
        Console.WriteLine("Escribe el número 1");
        string input1 = Console.ReadLine() ?? "0";
        int numeroA = Convert.ToInt32(input1);
        int resultado4 = (numeroA % 2);

        Console.WriteLine((resultado4 == 1) ? "GNU" : "\n");
        
    }
}
