
using System;
using System.Collections.Generic;

/* 
    3. Crea un array/lista con cinco elementos de tipo número real y multiplica todos sus elementos e imprime el resultado por pantalla.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> array = new List<int>();
        array.AddRange(new int[] { 1, 2, 3, 4, 5 });
        int multiplicacion = array[0] * array[1] * array[2] * array[3] * array[4];

        Console.WriteLine($"Multiplicacion total: {multiplicacion}");

    }
}
