
using System;
using System.Collections.Generic;

/* 
    17. Dada una lista impar de enteros ordenados, muestra la mediana.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> array = new List<int>();

        Console.WriteLine("Escribe un número:   ");
        array.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));
        Console.WriteLine("Escribe un número:   ");
        array.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));
        Console.WriteLine("Escribe un número:   ");
        array.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));
        Console.WriteLine("Escribe un número:   ");
        array.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));
        Console.WriteLine("Escribe un número:   ");
        array.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));
        Console.WriteLine("Escribe un número:   ");
        array.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));
        Console.WriteLine("Escribe un número:   ");
        array.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));


        array.Sort();
        double mediana = array[array.Count / 2];



        Console.WriteLine($"Mediana: {mediana}");



    }
}