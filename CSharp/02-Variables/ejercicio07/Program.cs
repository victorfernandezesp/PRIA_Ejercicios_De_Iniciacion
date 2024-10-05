
using System;

/* 
    7. Inicializa una variable radio y calcula el área de un círculo guardando el resultado en la variable area. Fórmula: п · radio · radio.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        double radio = 18.33;
        double area = 2 * Math.PI * (Math.Pow(radio, 2));
        Console.WriteLine("Área: " + area);
    }
}
