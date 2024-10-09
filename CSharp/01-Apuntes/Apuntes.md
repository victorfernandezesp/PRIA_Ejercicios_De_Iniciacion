# **PRIA 2024/2025**
**Víctor Fernandez España**


---
## COMANDOS DE CONSOLA

### Para crear proyecto:
```
    dotnet new console -o NOMBREPROYECTO
```

### Ejecutar programa desde la terminal (Tendriamos que estar en la ruta del programa): 
```
    dotnet run
```

-----

## ESENCIALES PARA CREAR EL PRIMER PROGRAMA
### Sintaxis para crear un programa
```
        using System; //ESTO VA PRIMERO SIEMPRE
        class Program
        {
            static void Main()
            {
                //APARTIR DE AQUI SE PROGRAMA
                int variable = 33;
                Console.WriteLine("Hola su número es " + variable);
            }
        }
```
## COMENTARIOS
#### COMENTARIO ¿QUÉ ES?

Un comentario en programación es un texto que se incluye en el código fuente de un programa, pero que no es ejecutado por la computadora. Los comentarios se utilizan para añadir explicaciones, anotaciones o notas dentro del código, lo que ayuda a los programadores a entender mejor el código que han escrito o el código de otros. Los comentarios son útiles para documentar el propósito de ciertas partes del código, aclarar lógica compleja, o simplemente dejar recordatorios para el futuro.

#### 1. Comentarios de una sola línea
Se usan para escribir comentarios breves en una sola línea. Para esto, se utiliza //.
```
    // Esto es un comentario en 1 línea.
```

#### 2. Comentarios de múltiples líneas
Se utilizan cuando quieres hacer un comentario más largo o comentar varias líneas de código a la vez. Para esto, se utiliza /* */.
```
    /* 
        Esto es un comentario en varias líneas
        Hola 
    */
```


## VARIABLES
#### TIPOS DE DATOS

```
    int: Enteros (números sin decimales)
    double: Números con decimales ( + precision)
    float: Números con decimales (menor precisión, se debe agregar 'f' al final)
    bool: Valores lógicos (true o false)
    char: Un solo carácter ('a', 'b', etc.)
    string: Cadena de caracteres
```

#### DECLARACIÓN DE VARIABLES
```
    int edad = 25;            // Entero
    double altura = 1.75;     // Decimal (mayor precisión)
    float peso = 70.5f;       // Decimal (menor precisión, se debe agregar 'f' al final)
    bool esMayor = true;      // Booleano (verdadero o falso)
    string nombre = "Juan";   // Cadena de texto (string)
    char inicial = 'J';       // Carácter (un solo carácter)
```