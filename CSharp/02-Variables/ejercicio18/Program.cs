
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
        Console.WriteLine(new string('G', resultado1) + new string('N', resultado1) + new string('U', resultado1));

        int numero2 = 4;
        int resultado2 = (numero2 % 2);
        Console.WriteLine(new string('G', resultado2) + new string('N', resultado2) + new string('U', resultado2));

        
        int numero3 = 11;
        int resultado3 = (numero3 % 2);
        Console.WriteLine(new string('G', resultado3) + new string('N', resultado3) + new string('U', resultado3));
        




        // Pasando como parámetros
        Console.WriteLine("Escribe el número 1");
        string input1 = Console.ReadLine() ?? "0";
        int numeroA = Convert.ToInt32(input1);
        int resultado4 = (numeroA % 2);

        Console.WriteLine(new string('G', resultado4) + new string('N', resultado4) + new string('U', resultado4));
        
    }
}
