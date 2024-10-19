using System;

/* 
    13. Dado cinco enteros, devuelve verdadero si aparece alguna vez 3 enteros impares consecutivos.

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

        bool esImpar1 = entero1 % 2 == 1;
        bool esImpar2 = entero2 % 2 == 1;
        bool esImpar3 = entero3 % 2 == 1;
        bool esImpar4 = entero4 % 2 == 1;
        bool esImpar5 = entero5 % 2 == 1;

        if (esImpar1 && esImpar2 && esImpar3)
        {
            Console.WriteLine("True");
        }
        else if (esImpar2 && esImpar3 && esImpar4)
        {
            Console.WriteLine("True");
        }
        else if (esImpar3 && esImpar4 && esImpar5)
        {
            Console.WriteLine("True");
        }
        else
        {
            Console.WriteLine("False");
        }
    }
}
