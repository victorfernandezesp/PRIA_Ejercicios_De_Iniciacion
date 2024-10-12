
using System;
using System.Collections.Generic;

/* 
    5. Crea un array/lista con cinco elementos e inserta en el primer índice, tercero y último tres números. Por último, imprime de nuevo el array, o lista,.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> array = new List<int>();
        array.AddRange(new int[] { 1, 2, 3, 4, 5 });

        Console.WriteLine("Array sin modificar: " + string.Join(", ", array));
        array.Insert(1, 8);
        array.Insert(3, 7);
        array.Reverse();
        array.Insert(0, 6);
        array.Reverse();
        Console.WriteLine("Array modificado: " + string.Join(", ", array));

    }
}
