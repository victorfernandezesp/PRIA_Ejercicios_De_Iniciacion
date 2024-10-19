using System;
using System.Collections.Generic;

/* 
    4. Crear un programa que determine si un número es menor que 0, o que está entre 0 y 50, o entre 51 y 100 o por encima de 100.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        int a = 56;

        if (a < 0)
        {
            Console.WriteLine("Es menor que 0");
        }
        else if (a >= 0 && a <= 50)
        {
            Console.WriteLine("Está entre 0 y 50");
        }
        else if (a >= 51 && a <= 100)
        {
            Console.WriteLine("Está entre 51 y 100");
        }
        else
        {
            Console.WriteLine("Es mayor a 100");
        }
    }
}
