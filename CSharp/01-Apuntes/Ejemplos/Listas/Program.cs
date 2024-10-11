        using System; //ESTO VA PRIMERO SIEMPRE
        class Program
        {
            static void Main()
            {
                int a = 5;
                float b = -3.4f;
                double c = -5.3;
                string cadena = "Pepe";
                bool booleano = true;

                // int x = 5;
                // int y = -4;

                // int z = x + y;
                // z = z - y;
                // Console.WriteLine(z);


                List<string> alimentos = new List<string> {"naranjas", "peras", "manzanas"};
                List<int> numeros = new List<int> {1, 2, 3};
            
                Console.WriteLine(alimentos.Count);

                Console.WriteLine(string.Join(", ", numeros));
                // Add e Instert(pos, elem) para insertar
                // Remove(Elemento)
                // GETRANFE
            
            }
        }