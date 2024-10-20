﻿
using System;
using System.Collections.Generic;

/* 
    13. Muestra la fila de una matriz 3x3 de enteros cuya suma de números sea la más alta.


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
        string input1 = Console.ReadLine() ?? "0";
        lista1.Add(Convert.ToInt32(Convert.ToDouble(input1)));

        Console.WriteLine("Escribe un número:   ");
        string input2 = Console.ReadLine() ?? "0";
        lista1.Add(Convert.ToInt32(Convert.ToDouble(input2)));

        Console.WriteLine("Escribe un número:   ");
        string input3 = Console.ReadLine() ?? "0";
        lista1.Add(Convert.ToInt32(Convert.ToDouble(input3)));

        Console.WriteLine("Escribe un número:   ");
        string input4 = Console.ReadLine() ?? "0";
        lista2.Add(Convert.ToInt32(Convert.ToDouble(input4)));

        Console.WriteLine("Escribe un número:   ");
        string input5 = Console.ReadLine() ?? "0";
        lista2.Add(Convert.ToInt32(Convert.ToDouble(input5)));

        Console.WriteLine("Escribe un número:   ");
        string input6 = Console.ReadLine() ?? "0";
        lista2.Add(Convert.ToInt32(Convert.ToDouble(input6)));

        Console.WriteLine("Escribe un número:   ");
        string input7 = Console.ReadLine() ?? "0";
        lista3.Add(Convert.ToInt32(Convert.ToDouble(input7)));

        Console.WriteLine("Escribe un número:   ");
        string input8 = Console.ReadLine() ?? "0";
        lista3.Add(Convert.ToInt32(Convert.ToDouble(input8)));

        Console.WriteLine("Escribe un número:   ");
        string input9 = Console.ReadLine() ?? "0";
        lista3.Add(Convert.ToInt32(Convert.ToDouble(input9)));


        listaDeListas.Add(lista1);
        listaDeListas.Add(lista2);
        listaDeListas.Add(lista3);


        Console.WriteLine("Matriz 3x3:");
        Console.WriteLine($"{listaDeListas[0][0]} {listaDeListas[0][1]} {listaDeListas[0][2]}");
        Console.WriteLine($"{listaDeListas[1][0]} {listaDeListas[1][1]} {listaDeListas[1][2]}");
        Console.WriteLine($"{listaDeListas[2][0]} {listaDeListas[2][1]} {listaDeListas[2][2]}");

        List<int> mayorsuma = listaDeListas.OrderByDescending(fila => fila.Sum()).First();

        Console.WriteLine($"La fila con la suma más alta es: {string.Join(", ", mayorsuma)}");


    }
}