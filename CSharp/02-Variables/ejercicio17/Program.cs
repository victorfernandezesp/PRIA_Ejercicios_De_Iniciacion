
using System;

/* 
    17. Dados cinco enteros, indica con un 0 si el número es par y con un 1 si el número es impar.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        // Sin pasar como parámetros
        int numero1 = 2;
        int numero2 = 25;
        int numero3 = 34;
        int numero4 = 22;
        int numero5 = 13;
        Console.WriteLine((numero1%2) + " " +(numero2%2) + " " +(numero3%2) + " " +(numero4%2) + " " +(numero5%2) );
       
        int numero6 = 232;
        int numero7 = 7;
        int numero8 = 23;
        int numero9 = 14;
        int numero10 = 40;
        Console.WriteLine((numero6%2) + " " +(numero7%2) + " " +(numero8%2) + " " +(numero9%2) + " " +(numero10%2) );
       
        int numero11 = 5;
        int numero12 = 9;
        int numero13 = 37;
        int numero14 = 2;
        int numero15 = 3;
        Console.WriteLine((numero11%2) + " " +(numero12%2) + " " +(numero13%2) + " " +(numero14%2) + " " +(numero15%2) );

        


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

        Console.WriteLine("Escribe el número 4");
        string input4 = Console.ReadLine() ?? "0";
        int numeroD = Convert.ToInt32(input4);

        Console.WriteLine("Escribe el número 5");
        string input5 = Console.ReadLine() ?? "0";
        int numeroE = Convert.ToInt32(input5);

        Console.WriteLine((numeroA%2) + " " +(numeroB%2) + " " +(numeroC%2) + " " +(numeroD%2) + " " +(numeroE%2) );

    }
}
