using System;
using System.Collections.Generic;

/* 
    12. En una matriz 3x3 de enteros, muestra la suma más alta de los números de una fila.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        List<List<int>> listaDeListas = new List<List<int>>();
        List<int> lista1 = new List<int>();
        List<int> lista2 = new List<int>();
        List<int> lista3 = new List<int>();

        Console.WriteLine("Escribe un número:   ");
        lista1.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        Console.WriteLine("Escribe un número:   ");
        lista1.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        Console.WriteLine("Escribe un número:   ");
        lista1.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        Console.WriteLine("Escribe un número:   ");
        lista2.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        Console.WriteLine("Escribe un número:   ");
        lista2.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        Console.WriteLine("Escribe un número:   ");
        lista2.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        Console.WriteLine("Escribe un número:   ");
        lista3.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        Console.WriteLine("Escribe un número:   ");
        lista3.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        Console.WriteLine("Escribe un número:   ");
        lista3.Add(Convert.ToInt32(Console.ReadLine() ?? "0"));

        listaDeListas.Add(lista1);
        listaDeListas.Add(lista2);
        listaDeListas.Add(lista3);

        Console.WriteLine("Matriz 3x3:");
        Console.WriteLine($"{listaDeListas[0][0]} {listaDeListas[0][1]} {listaDeListas[0][2]}");
        Console.WriteLine($"{listaDeListas[1][0]} {listaDeListas[1][1]} {listaDeListas[1][2]}");
        Console.WriteLine($"{listaDeListas[2][0]} {listaDeListas[2][1]} {listaDeListas[2][2]}");

        int sumaFila1 = listaDeListas[0][0] + listaDeListas[0][1] + listaDeListas[0][2];
        int sumaFila2 = listaDeListas[1][0] + listaDeListas[1][1] + listaDeListas[1][2];
        int sumaFila3 = listaDeListas[2][0] + listaDeListas[2][1] + listaDeListas[2][2];

        int sumaMaxima = Math.Max(sumaFila1, Math.Max(sumaFila2, sumaFila3));
        Console.WriteLine($"La suma más alta de las filas es: {sumaMaxima}");
    }
}
