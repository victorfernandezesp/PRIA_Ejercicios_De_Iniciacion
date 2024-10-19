
using System;
using System.Collections.Generic;

/* 
    3. Crea un programa que determine si una variable de tipo numérico es positiva, negativa o cero.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        int a = -2;

        if (a > 0)
        {
            Console.WriteLine("Es mayor que 0");
        }
        else if (a < 0)
        {
            Console.WriteLine("Es menor que 0");
        }
        else
        {
            Console.WriteLine("Es igual a 0");
        }


    }
}
