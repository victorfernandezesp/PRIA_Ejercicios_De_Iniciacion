
using System;
using System.Collections.Generic;

/* 
    14. Dado un número con más de 10 dígitos, suma los 3 primeros dígitos y los 3 últimos dígitos.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        Console.Write("Introduce un número: ");
        string numero = Console.ReadLine() ?? "";

        List<int> array = new List<int>();
        foreach (char digit in numero)
        {
            array.Add(int.Parse(digit.ToString()));
        }

        Console.WriteLine($"Array: [{string.Join(", ", array)}]");

        int suma = array[0] + array[1] + array[2] 
                   + array[array.Count - 1] 
                   + array[array.Count - 2] 
                   + array[array.Count - 3];

        Console.WriteLine($"La suma es: {suma}");


    }
}