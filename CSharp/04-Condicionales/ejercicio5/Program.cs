using System;

/* 
    5. Crea un programa que determine si una letra es vocal o consonante.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        string vocales = "AEIOUaeiouáéíóúÁÉÍÓÚ";
        char letra = 'e';

        if (vocales.Contains(letra))
        {
            Console.WriteLine("Es Vocal");
        }
        else
        {
            Console.WriteLine("Es Consonante");
        }
    }
}
