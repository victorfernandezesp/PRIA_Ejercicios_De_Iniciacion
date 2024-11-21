
using System;
using System.Collections.Generic;

/* 
    1. Convierte π/6, π/4, π/3, π/2, 2π/3, 3π/4, π, 3π/2 y 2π radianes a grados (fórmula) en GDScript y C#.

    @author Victor Fernandez España
*/


class Programa
{
    static void Main()
    {
        double[] radianes = { Math.PI / 6, Math.PI / 4, Math.PI / 3, Math.PI / 2, 2 * Math.PI / 3, 3 * Math.PI / 4, Math.PI, 3 * Math.PI / 2, 2 * Math.PI };
        List<double> grados = new List<double>();

        foreach (double rad in radianes)
        {
            grados.Add(rad * 180 / Math.PI);
        }

        foreach (double grado in grados)
        {
            Console.WriteLine(grado);
        }

    }
}
