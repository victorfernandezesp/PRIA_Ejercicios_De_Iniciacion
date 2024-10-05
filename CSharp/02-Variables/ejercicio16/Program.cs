
using System;

/* 
    16. Dado un entero, indica con un 0 si el número es par y con un 1 si el número es impar.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        // Sin pasar como parámetros
        int numero1 = 2;
        Console.WriteLine("Es: " + (numero1%2));
       
        int numero2 = 7;
        Console.WriteLine("Es: " + (numero2%2));

        int numero3 = 10;
        Console.WriteLine("Es: " + (numero3%2));
        


        // Pasando como parámetros
        Console.WriteLine("Escribe el número 1");
        string input1 = Console.ReadLine() ?? "0";
        int numeroA = Convert.ToInt32(input1);

        Console.WriteLine("Es: " + (numeroA%2));
        

    }
}
