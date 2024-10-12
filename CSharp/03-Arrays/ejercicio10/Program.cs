
using System;
using System.Collections.Generic;

/* 
    10. Crea un array/lista de números de tipo número real, ordénalos al revés e imprime dicho array, o lista, por pantalla.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> array = new List<int>();
        array.AddRange(new int[] { 3, 2, 4, 1, 5});
        Console.WriteLine($"Array sin ordenar:  {string.Join(", ", array)} ");
        array.Sort();
        array.Reverse();
        Console.WriteLine($"Array ordenado:     {string.Join(", ", array)} ");


    }
}