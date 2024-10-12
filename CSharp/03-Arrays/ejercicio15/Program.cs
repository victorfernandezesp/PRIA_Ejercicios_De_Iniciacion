
using System;
using System.Collections.Generic;

/* 
    15. Dada una serie de palabras, ordénalas alfabéticamente.




    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<string> array = new List<string>();

        Console.WriteLine("Escribe una palabra:   ");
        array.Add(Console.ReadLine() ?? "0");
        Console.WriteLine("Escribe una palabra:   ");
        array.Add(Console.ReadLine() ?? "0");
        Console.WriteLine("Escribe una palabra:   ");
        array.Add(Console.ReadLine() ?? "0");
        Console.WriteLine("Escribe una palabra:   ");
        array.Add(Console.ReadLine() ?? "0");
        

        array.Sort();


        Console.WriteLine($"Array: [{string.Join(", ", array)}]");



    }
}