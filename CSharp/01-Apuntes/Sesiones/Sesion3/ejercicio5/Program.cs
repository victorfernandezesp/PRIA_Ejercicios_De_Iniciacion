using System;

/* 
   Calcula en C# y Python la distancia y el punto medio entre A(-3, 4, -2) y B(2, 6, 3) en el espacio 3D.
   
   @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        double[] A = { -3, 4, -2 };
        double[] B = { 2, 6, 3 };

        double distancia = Math.Sqrt(
            Math.Pow(B[0] - A[0], 2) + Math.Pow(B[1] - A[1], 2) + Math.Pow(B[2] - A[2], 2)
        );

        double[] punto_medio = {
            (A[0] + B[0]) / 2,
            (A[1] + B[1]) / 2,
            (A[2] + B[2]) / 2
        };

        Console.WriteLine("La distancia entre A y B es: " + distancia);
        Console.WriteLine("El punto medio entre A y B es: (" + punto_medio[0] + ", " + punto_medio[1] + ", " + punto_medio[2] + ")");
    }
}
