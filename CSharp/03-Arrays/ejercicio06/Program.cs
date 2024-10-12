
using System;
using System.Collections.Generic;

/* 
    6. Convierte un array/lista de números que sean de tipo cadena de caracteres a tipo número real.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<string> array = new List<string>();
        array.AddRange(new string[] { "1", "2", "3", "4", "5" });

        Console.WriteLine("Array sin modificar: " + string.Join(", ", array));
        List<int> arrayNumeros = array.ConvertAll(int.Parse);

        Console.WriteLine("Array modificado: " + string.Join(", ", array));

    }
}
