
using System;
using System.Collections.Generic;

/* 
    7. Crea un array/lista e imprime en pantalla el número de elementos.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<string> array = new List<string>();
        array.AddRange(new string[] { "1", "2", "3", "4", "5" });

        Console.WriteLine($"Elementos: {array.Count()}");
        

    }
}
