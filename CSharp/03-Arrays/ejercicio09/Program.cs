
using System;
using System.Collections.Generic;

/* 
    9. Crea un array/lista de números de tipo cadena de caracteres, ordénalos e imprime dicho array, o lista, por pantalla.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> array = new List<int>();
        array.AddRange(new int[] { "5", "2", "1", "4", "3" });
        Console.WriteLine($"Array sin ordenar:  {string.Join(", ", array)} ");
        array.Sort();
        Console.WriteLine($"Array ordenado:     {string.Join(", ", array)} ");


    }
}
