using System;

/* 
    14. Elimina todas las vocales dada una cadena, o string, de cinco caracteres.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        Console.Write("Introduce una cadena de 5 caracteres: ");
        string cadena = Console.ReadLine();
        string vocales = "AEIOUaeiouáéíóúÁÉÍÓÚ";

        if (cadena.Length != 5)
        {
            Console.WriteLine("Tiene que tener 5 caracteres.");
        }
        else
        {
            if (vocales.Contains(cadena[0]))
                cadena = cadena.Replace(cadena[0].ToString(), "", 1);
            if (vocales.Contains(cadena[1]))
                cadena = cadena.Replace(cadena[1].ToString(), "", 1);
            if (vocales.Contains(cadena[2]))
                cadena = cadena.Replace(cadena[2].ToString(), "", 1);
            if (vocales.Contains(cadena[3]))
                cadena = cadena.Replace(cadena[3].ToString(), "", 1);
            if (vocales.Contains(cadena[4]))
                cadena = cadena.Replace(cadena[4].ToString(), "", 1);

            Console.WriteLine($"Cadena sin vocales: {cadena}");
        }
    }
}
