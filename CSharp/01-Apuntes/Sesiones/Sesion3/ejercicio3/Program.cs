using System;

/* 
   Resuelve en C# y Python los dos ejercicios de este vídeo sobre el teorema de Pitágoras (fórmula).
   
   @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        double[] punto1_2D = { 1, 2 };
        double[] punto2_2D = { 3, 4 };

        double distancia_2D = Math.Sqrt(
            Math.Pow(punto2_2D[0] - punto1_2D[0], 2) + Math.Pow(punto2_2D[1] - punto1_2D[1], 2)
        );

        double[] punto1_3D = { 1, 2, 3 };
        double[] punto2_3D = { 4, 6, 8 };

        double distancia_3D = Math.Sqrt(
            Math.Pow(punto2_3D[0] - punto1_3D[0], 2)
            + Math.Pow(punto2_3D[1] - punto1_3D[1], 2)
            + Math.Pow(punto2_3D[2] - punto1_3D[2], 2)
        );

        Console.WriteLine("La distancia entre los puntos en 2D es: " + distancia_2D);
        Console.WriteLine("La distancia entre los puntos en 3D es: " + distancia_3D);
    }
}
