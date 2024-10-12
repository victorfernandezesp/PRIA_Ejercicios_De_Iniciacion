
using System;
using System.Collections.Generic;

/* 
    11. A partir de 5 números, muestra aquellos que no sean el mayor ni el menor y ordenados de mayor a menor.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> array = new List<int>();

        Console.WriteLine("Escribe un número:   ");
        string input1 = Console.ReadLine() ?? "0";
        int numeroA = Convert.ToInt32(Convert.ToDouble(input1));

        Console.WriteLine("Escribe un número:   ");
        string input2 = Console.ReadLine() ?? "0";
        int numeroB = Convert.ToInt32(Convert.ToDouble(input2));

        Console.WriteLine("Escribe un número:   ");
        string input3 = Console.ReadLine() ?? "0";
        int numeroC = Convert.ToInt32(Convert.ToDouble(input3));

        Console.WriteLine("Escribe un número:   ");
        string input4 = Console.ReadLine() ?? "0";
        int numeroD = Convert.ToInt32(Convert.ToDouble(input4));

        Console.WriteLine("Escribe un número:   ");
        string input5 = Console.ReadLine() ?? "0";
        int numeroE = Convert.ToInt32(Convert.ToDouble(input5));

        array.Add(numeroA);
        array.Add(numeroB);
        array.Add(numeroC);
        array.Add(numeroD);
        array.Add(numeroE);


        Console.WriteLine($"Array sin ordenar:  {string.Join(", ", array)} ");
        array.Sort();
        array.RemoveAt(array.Count-1);
        array.Reverse();
        array.RemoveAt(array.Count-1);
        array.Reverse();
        array.Reverse();

        Console.WriteLine($"Array ordenado:     {string.Join(", ", array)} ");


    }
}