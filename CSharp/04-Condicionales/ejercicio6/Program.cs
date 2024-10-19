using System;

/* 
    6. Crea un programa que determine si, dado sus tres ángulos, se puede formar un triángulo (pista: un triángulo se forma cuando sus tres ángulos suman 180º).

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        int angulo1 = 55;
        int angulo2 = 100;
        int angulo3 = 60;

        if ((angulo1 + angulo2 + angulo3) == 180)
        {
            Console.WriteLine("Es Triángulo");
        }
        else
        {
            Console.WriteLine("No es triángulo");
        }
    }
}
