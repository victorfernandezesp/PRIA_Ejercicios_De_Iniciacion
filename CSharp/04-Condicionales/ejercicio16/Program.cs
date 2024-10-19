using System;

/* 
    16. Dadas dos series de tres enteros, comprueba si todos los enteros de la primera serie aparecen en alguno de los enteros de la segunda serie.

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

        Console.Write("Introduce un número: ");
        int entero4 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero5 = int.Parse(Console.ReadLine());

        Console.Write("Introduce un número: ");
        int entero6 = int.Parse(Console.ReadLine());

        bool primeroEnSegunda = entero1 == entero4 || entero1 == entero5 || entero1 == entero6;
        bool segundoEnSegunda = entero2 == entero4 || entero2 == entero5 || entero2 == entero6;
        bool terceroEnSegunda = entero3 == entero4 || entero3 == entero5 || entero3 == entero6;

        if (primeroEnSegunda && segundoEnSegunda && terceroEnSegunda)
        {
            Console.WriteLine("Sí.");
        }
        else
        {
            Console.WriteLine("No.");
        }
    }
}
