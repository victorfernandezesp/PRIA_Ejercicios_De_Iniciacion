
using System;

/* 
    6. Inicializa una variable radio y calcula la circunferencia guardando el resultado en la variable circunferencia. Fórmula: 2 · п · radio.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        double radio = 18.33;
        double circunferencia = 2 * Math.PI *radio;
        Console.WriteLine("Cincunferencia: " + circunferencia);
    }
}
