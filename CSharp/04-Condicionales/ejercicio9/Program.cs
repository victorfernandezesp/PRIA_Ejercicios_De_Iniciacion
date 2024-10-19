using System;

/* 
    9. Crea un programa que imprima por orden alfabético tres cadenas de caracteres o strings dados y que imprima si son o no iguales dichos tres strings.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        string cadena1 = "Hola";
        string cadena2 = "Holaa";
        string cadena3 = "Holaaa";

        string[] arrayOrden = { cadena1, cadena2, cadena3 };
        Array.Sort(arrayOrden);

        Console.WriteLine($"Ordenado: {string.Join(", ", arrayOrden)}");

        if (cadena1 == cadena2 && cadena2 == cadena3)
        {
            Console.WriteLine("Las cadenas SON iguales.");
        }
        else
        {
            Console.WriteLine("Las cadenas NO son iguales.");
        }
    }
}
