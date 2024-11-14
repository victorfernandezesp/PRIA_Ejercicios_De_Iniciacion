using System;

/* 
    Programa en C# y Python las fórmulas del punto medio para dos puntos 2D y 3D y haz ejemplos.

   
    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        double x1 = 1, y1 = 2, z1 = 3;
        double x2 = 4, y2 = 5, z2 = 6;

        double mx2D = (x1 + x2) / 2;
        double my2D = (y1 + y2) / 2;

        double mx3D = (x1 + x2) / 2;
        double my3D = (y1 + y2) / 2;
        double mz3D = (z1 + z2) / 2;

        Console.WriteLine("Punto Medio 2D: (" + mx2D + ", " + my2D + ")");
        Console.WriteLine("Punto Medio 3D: (" + mx3D + ", " + my3D + ", " + mz3D + ")");
    }
}
