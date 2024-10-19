using System;

/* 
    15. Detecta la primera aparición de un entero a partir de una serie de cinco enteros devolviendo el índice con su posición.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        Console.Write("Introduce el número a buscar: ");
        int entero1 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero2 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero3 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero4 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero5 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero6 = int.Parse(Console.ReadLine());

        int[] array = { entero2, entero3, entero4, entero5, entero6 };

        if (entero1 == array[0])
        {
            Console.WriteLine("1");
        }
        else if (entero1 == array[1])
        {
            Console.WriteLine("2");
        }
        else if (entero1 == array[2])
        {
            Console.WriteLine("3");
        }
        else if (entero1 == array[3])
        {
            Console.WriteLine("4");
        }
        else if (entero1 == array[4])
        {
            Console.WriteLine("5");
        }
        else
        {
            Console.WriteLine("No está el número.");
        }
    }
}
