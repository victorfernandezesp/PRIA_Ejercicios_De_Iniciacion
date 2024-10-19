using System;

/* 
    18. Dados dos enteros positivos, imprime el valor más cercano a 21 sin sobrepasarse. Imprime 0 si los dos enteros son mayores que 21.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        Console.Write("Introduce un número: ");
        int numero1 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int numero2 = int.Parse(Console.ReadLine());

        if (numero1 > 21 && numero2 > 21)
        {
            Console.WriteLine("0");
        }
        else if (numero1 <= 21 && numero2 <= 21)
        {
            Console.WriteLine(Math.Max(numero1, numero2));
        }
        else
        {
            Console.WriteLine(Math.Min(numero1, numero2));
        }
    }
}
