using System;

/* 
    11. Dado dos enteros, calcula la suma. Si el resultado está entre 10 y 19 (ambos incluidos), imprime 20. Si no, imprime la suma.

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

        int resultado = entero1 + entero2;

        if (resultado >= 10 && resultado <= 19)
        {
            Console.WriteLine("20.");
        }
        else
        {
            Console.WriteLine($"{resultado}.");
        }
    }
}
