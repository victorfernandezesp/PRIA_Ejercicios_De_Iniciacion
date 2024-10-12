
using System;
using System.Collections.Generic;

/* 
    4. Crea un array/lista con cinco elementos y elimina el primer, tercer y último elemento. Por último, imprime de nuevo el array, o lista,.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> array = new List<int>();
        array.AddRange(new int[] { 1, 2, 3, 4, 5 });

        Console.WriteLine("Array sin modificar: " + string.Join(", ", array));
        array.RemoveAt(4);
        array.RemoveAt(2);
        array.RemoveAt(0);
        Console.WriteLine("Array modificado: " + string.Join(", ", array));

    }
}
