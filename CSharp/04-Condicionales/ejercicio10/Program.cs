using System;

/* 
    10. Crea un programa que determine si una persona está en edad de trabajar.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        int edadPersona = 15;

        if (edadPersona >= 16 && edadPersona <= 65)
        {
            Console.WriteLine("Está en edad de trabajar.");
        }
        else
        {
            Console.WriteLine("No está en edad de trabajar.");
        }
    }
}
