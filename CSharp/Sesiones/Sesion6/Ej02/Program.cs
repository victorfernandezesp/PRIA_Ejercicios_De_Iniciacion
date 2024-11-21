
using System;
using System.Collections.Generic;

/* 
    2. Convierte 30°, 45°, 60°, 90°, 120°, 135°, 180°, 270° y 360° a radianes (fórmula) en GDScript y C#.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        int[] grados = { 30, 45, 60, 90, 120, 135, 180, 270, 360 };
        List<double> radianes = new List<double>();

        foreach (int grado in grados)
        {
            radianes.Add(grado * Math.PI / 180);
        }

        foreach (double radian in radianes)
        {
            Console.WriteLine(radian);
        }
    }
}
