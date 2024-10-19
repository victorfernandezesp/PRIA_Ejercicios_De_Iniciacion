using System;

/* 
    19. Determina en una partida finalizada de tres en raya si gana O, gana X o hay empate.

    @author Victor Fernandez España
*/

class Programa
{
    static void Main()
    {
        string[][] tablero = new string[3][];
        tablero[0] = new string[3];
        tablero[1] = new string[3];
        tablero[2] = new string[3];

        Console.Write("Introduce (X/O) para la posición [0,0]: ");
        tablero[0][0] = Console.ReadLine();
        Console.Write("Introduce (X/O) para la posición [0,1]: ");
        tablero[0][1] = Console.ReadLine();
        Console.Write("Introduce (X/O) para la posición [0,2]: ");
        tablero[0][2] = Console.ReadLine();
        
        Console.Write("Introduce (X/O) para la posición [1,0]: ");
        tablero[1][0] = Console.ReadLine();
        Console.Write("Introduce (X/O) para la posición [1,1]: ");
        tablero[1][1] = Console.ReadLine();
        Console.Write("Introduce (X/O) para la posición [1,2]: ");
        tablero[1][2] = Console.ReadLine();
        
        Console.Write("Introduce (X/O) para la posición [2,0]: ");
        tablero[2][0] = Console.ReadLine();
        Console.Write("Introduce (X/O) para la posición [2,1]: ");
        tablero[2][1] = Console.ReadLine();
        Console.Write("Introduce (X/O) para la posición [2,2]: ");
        tablero[2][2] = Console.ReadLine();

        string ganador = "";

        if (tablero[0][0] == tablero[0][1] && tablero[0][1] == tablero[0][2] && tablero[0][0] != "")
            ganador = tablero[0][0];
        else if (tablero[1][0] == tablero[1][1] && tablero[1][1] == tablero[1][2] && tablero[1][0] != "")
            ganador = tablero[1][0];
        else if (tablero[2][0] == tablero[2][1] && tablero[2][1] == tablero[2][2] && tablero[2][0] != "")
            ganador = tablero[2][0];
        else if (tablero[0][0] == tablero[1][0] && tablero[1][0] == tablero[2][0] && tablero[0][0] != "")
            ganador = tablero[0][0];
        else if (tablero[0][1] == tablero[1][1] && tablero[1][1] == tablero[2][1] && tablero[0][1] != "")
            ganador = tablero[0][1];
        else if (tablero[0][2] == tablero[1][2] && tablero[1][2] == tablero[2][2] && tablero[0][2] != "")
            ganador = tablero[0][2];
        else if (tablero[0][0] == tablero[1][1] && tablero[1][1] == tablero[2][2] && tablero[0][0] != "")
            ganador = tablero[0][0];
        else if (tablero[0][2] == tablero[1][1] && tablero[1][1] == tablero[2][0] && tablero[0][2] != "")
            ganador = tablero[0][2];
        else
            ganador = "Empate";


        if (ganador == "Empate")
            Console.WriteLine("Empate.");
        else
            Console.WriteLine($"Ha ganado: {ganador}");
    }
}
