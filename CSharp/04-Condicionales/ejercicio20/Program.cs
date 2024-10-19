using System;

/* 
    20. Determina si un entero (mayor que 0 y menor que 10 000) al leerlo contiene la palabra cinco.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        Console.Write("Introduce un número entero mayor que 0 y menor que 10,000: ");
        int numero = int.Parse(Console.ReadLine());

        int[] numerosNoSeLeenComoCinco = {
            15, 150, 251, 350, 500, 515, 750,
            751, 752, 753, 754, 756, 757, 758,
            759, 850, 851, 852, 853, 854, 856,
            857, 858, 859, 950, 951, 952, 953,
            954, 956, 957, 958, 959
        };

        if (0 < numero && numero < 10000)
        {
            string numeroStr = numero.ToString();

            if (numeroStr.Contains("5") && Array.IndexOf(numerosNoSeLeenComoCinco, numero) == -1)
            {
                Console.WriteLine("Sí.");
            }
            else
            {
                Console.WriteLine("No.");
            }
        }
        else
        {
            Console.WriteLine("Número fuera de rango.");
        }
    }
}
