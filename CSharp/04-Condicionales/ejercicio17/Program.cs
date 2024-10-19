using System;

/* 
    17. Convierte de centímetros a metros y viceversa.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        Console.Write("Introduce un número: ");
        float numero1 = float.Parse(Console.ReadLine());
        
        Console.Write("Introduce la medida (cm/m): ");
        string medida2 = Console.ReadLine();

        if (medida2 != "cm" && medida2 != "m")
        {
            Console.WriteLine("La medida introducida no es correcta.");
        }
        else
        {
            if (medida2 == "cm")
            {
                numero1 *= 0.01f;
                Console.WriteLine($"La conversión da: {numero1}m");
            }
            else
            {
                numero1 *= 100;
                Console.WriteLine($"La conversión da: {numero1}cm");
            }
        }
    }
}
