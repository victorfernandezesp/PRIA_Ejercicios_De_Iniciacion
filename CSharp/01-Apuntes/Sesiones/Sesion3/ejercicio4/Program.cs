using System;

/* 
   Calcula en C# y Python la distancia y el punto medio entre los puntos (-1, -3) y (5, 7) en el espacio 2D.
   
   @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        double[] punto1 = { -1, -3 };
        double[] punto2 = { 5, 7 };

        double distancia = Math.Sqrt(
            Math.Pow(punto2[0] - punto1[0], 2) + Math.Pow(punto2[1] - punto1[1], 2)
        );

        double[] punto_medio = {
            (punto1[0] + punto2[0]) / 2,
            (punto1[1] + punto2[1]) / 2
        };

        Console.WriteLine("La distancia entre los puntos es: " + distancia);
        Console.WriteLine("El punto medio entre los puntos es: (" + punto_medio[0] + ", " + punto_medio[1] + ")");
    }
}
