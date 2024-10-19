
using System;
using System.Collections.Generic;

/* 
    2. Crea un programa que determine si un número entero es par o impar (pista: usar la operación %).

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        int numeroa = 2;

        if (numeroa % 2)
        {
            Console.WriteLine($"Es par");
        }
        else
        {
            Console.WriteLine($"No es par");
        }

    }
}
