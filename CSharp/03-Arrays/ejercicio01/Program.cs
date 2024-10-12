
using System;
using System.Collections.Generic;

/* 
    1. Crea un array o una lista con cinco elementos e imprime en pantalla el primer, tercer y último elemento.



    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        List<int> numeros = new List<int>();
        numeros.AddRange(new int[] { 1, 2, 3, 4, 5 });

        Console.WriteLine($"Primer elemento {numeros[0]} Tercer elemento {numeros[2]} Ultimo Elemento {numeros[numeros.Count - 1]}");

    }
}
