using System;

/* 
    8. Crea un programa que encuentre el número mayor a partir de tres números dados.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        int numero1 = 60;
        int numero2 = 60;
        int numero3 = 40;

        if (numero1 > numero2 && numero1 > numero3)
        {
            Console.WriteLine($"{numero1} es el mayor.");
        }
        else if (numero2 > numero1 && numero2 > numero3)
        {
            Console.WriteLine($"{numero2} es el mayor.");
        }
        else if (numero3 > numero1 && numero3 > numero2)
        {
            Console.WriteLine($"{numero3} es el mayor.");
        }
        else
        {
            Console.WriteLine($"El mayor es: {Math.Max(Math.Max(numero1, numero2), numero3)}");
        }
    }
}
