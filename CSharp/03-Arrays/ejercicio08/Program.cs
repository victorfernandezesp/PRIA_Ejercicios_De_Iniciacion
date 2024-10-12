
using System;
using System.Collections.Generic;

/* 
    8. Crea un array/lista de números de tipo número real, ordénalos e imprime dicho array, o lista, por pantalla.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> array = new List<int>();
        array.AddRange(new int[] { 5, 2, 3, 1, 4 });
        Console.WriteLine($"Array sin ordenar:  {string.Join(", ", array)} ");
        array.Sort();
        Console.WriteLine($"Array ordenado:     {string.Join(", ", array)} ");


    }
}
