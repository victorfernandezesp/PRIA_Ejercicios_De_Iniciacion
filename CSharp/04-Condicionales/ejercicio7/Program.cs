using System;

/* 
    7. Crea un programa que determine a partir de dos números cuál es el mayor y cuál es el menor o que imprima que son iguales si así lo son.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        int numero1 = 60;
        int numero2 = 50;

        if (numero1 == numero2)
        {
            Console.WriteLine("Son iguales");
        }
        else if (numero1 > numero2)
        {
            Console.WriteLine($"{numero1} es mayor que {numero2}");
        }
        else
        {
            Console.WriteLine($"{numero2} es mayor que {numero1}");
        }
    }
}
