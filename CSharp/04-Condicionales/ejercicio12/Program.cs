using System;

/* 
    12. Dado tres enteros, devuelve verdadero si no aparece ni un 1 y ni un 3.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        Console.Write("Introduce un número: ");
        int entero1 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero2 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero3 = int.Parse(Console.ReadLine());

        if (entero1 != 1 && entero1 != 3 && entero2 != 1 && entero2 != 3 && entero3 != 1 && entero3 != 3)
        {
            Console.WriteLine("True");
        }
        else
        {
            Console.WriteLine("False");
        }
    }
}
