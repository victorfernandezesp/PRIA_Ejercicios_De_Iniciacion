using System;

/* 
   Resuelve en C# y Python los dos ejercicios de este vídeo sobre el teorema de Pitágoras (fórmula).
   
   @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        double cateto1 = 5, cateto2 = 6;
        double cateto3 = 20 * 10, cateto4 = 29 * 10;

        double hipotenusa1 = Math.Sqrt(Math.Pow(cateto1, 2) + Math.Pow(cateto2, 2));
        double hipotenusa2 = Math.Sqrt(Math.Pow(cateto3, 2) + Math.Pow(cateto4, 2));

        Console.WriteLine("La hipotenusa en el ejercicio a: " + hipotenusa1 + " m");
        Console.WriteLine("La hipotenusa en el ejercicio b: " + hipotenusa2 + " m");
    }
}
