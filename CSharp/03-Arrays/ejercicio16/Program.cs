
using System;
using System.Collections.Generic;

/* 
    16. Dada una serie de palabras, ordénalas alfabéticamente al revés (de z a a). A continuación, muestra el resultado final exceptuando la primera palabra y las tres últimas palabras.


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
        Console.WriteLine("Escribe una palabra:   ");
        array.Add(Console.ReadLine() ?? "0");
        Console.WriteLine("Escribe una palabra:   ");
        array.Add(Console.ReadLine() ?? "0");
        Console.WriteLine("Escribe una palabra:   ");
        array.Add(Console.ReadLine() ?? "0");
        

        array.Sort();
        array.Reverse();
        array.RemoveAt(0);
        array.RemoveAt(array.Count-1);
        array.RemoveAt(array.Count-1);
        array.RemoveAt(array.Count-1);


        Console.WriteLine($"Array: [{string.Join(", ", array)}]");



    }
}