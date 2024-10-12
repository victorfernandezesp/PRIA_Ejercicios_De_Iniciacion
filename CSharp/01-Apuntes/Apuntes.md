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

## IMPRIMIR POR PANTALLA
#### IMPRIMIR SOLO TEXTO
```
    Console.WriteLine("Hola Mundo");
```

#### IMPRIMIR CONTENIDO DE UNA VARIABLE
```
    int edad = 25;
    Console.WriteLine("La edad es: " + edad);

    Console.WriteLine($"La edad es: {edad} ");
```
## EXPRESIONES

#### 1. Expresiones Literales:
Son valores fijos que no cambian.  
Ejemplos:
- `5` (entero)
- `3.14` (decimal)
- `"Hola"` (cadena de texto)
- `'A'` (carácter)
- `true` o `false` (booleano)

#### 2. Expresiones de Variable:
Son expresiones que contienen una variable. El valor de la variable es el resultado de la expresión.  
Ejemplo:
```csharp
int x = 10;
var y = x;  // 'y' es una expresión que toma el valor de 'x', que es 10
```

#### 3. Expresiones Aritméticas:
Realizan operaciones matemáticas sobre valores numéricos.  
Ejemplos:
- `a + b` (suma)
- `x * 5` (multiplicación)
- `10 / 3` (división)
- `100 % 7` (módulo)

#### 4. Expresiones de Comparación:
Retornan un valor booleano (true o false).  
Operadores de comparación:
- `==` (igual)
- `!=` (diferente)
- `>` (mayor que)
- `<` (menor que)
- `>=` (mayor o igual)
- `<=` (menor o igual)

Ejemplo:
```csharp
int a = 5;
bool resultado = (a > 3);  // resultado es 'true'
```

#### 5. Expresiones Lógicas:
Combinan valores booleanos mediante operadores lógicos.  
Operadores lógicos:
- `&&` (Y lógico)
- `||` (O lógico)
- `!` (NO lógico)

Ejemplo:
```csharp
bool a = true;
bool b = false;
bool resultado = (a && b);  // resultado es 'false'
```

#### 6. Expresiones de Asignación:
El valor de una variable es asignado mediante el operador `=`.  
Ejemplo:
```csharp
int x = 5;
int y = x + 10;  // 'y' es asignado a 15, que es el resultado de la expresión 'x + 10'
```

#### 7. Expresiones Condicionales (Ternarias):
Es una forma abreviada de una instrucción `if-else`.  
Sintaxis:
```csharp
condición ? valor_si_true : valor_si_false;
```

Ejemplo:
```csharp
int edad = 18;
string mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
```

#### 8. Expresiones de Invocación de Métodos:
Invocan un método que devuelve un valor.  
Ejemplo:
```csharp
int suma = Math.Abs(-5);  // Llama al método 'Abs' de la clase Math, que devuelve 5
```

#### 9. Expresiones de Acceso a Propiedades o Campos:
Acceden a propiedades o campos de una clase, objeto o estructura.  
Ejemplo:
```csharp
string nombre = persona.Nombre;  // 'persona.Nombre' es una expresión que obtiene el valor de la propiedad 'Nombre'
```

#### 10. Expresiones Lambda:
Son una forma concisa de representar funciones anónimas.  
Sintaxis:
```csharp
(parametros) => expresión;
```

Ejemplo:
```csharp
Func<int, int, int> suma = (a, b) => a + b;
int resultado = suma(3, 4);  // resultado es 7
```

#### 11. Expresiones de Inicialización:
Permiten inicializar colecciones u objetos.  
Ejemplo de inicialización de una lista:
```csharp
List<int> lista = new List<int> { 1, 2, 3, 4, 5 };
```

#### 12. Expresiones de Type-Casting:
Permiten convertir un valor de un tipo a otro.  
Ejemplo:
```csharp
double pi = 3.14;
int piEntero = (int)pi;  // Pi se convierte en 3
```

#### 13. Expresiones de Null-Coalescing:
El operador de coalescencia nula (`??`) proporciona un valor por defecto si el primer valor es `null`.  
Ejemplo:
```csharp
string nombre = null;
string resultado = nombre ?? "Desconocido";  // 'resultado' será "Desconocido"
```


## OPERADORES ARITMETICOS

#### 1. Operadores Aritméticos:
Estos son los operadores que permiten realizar cálculos matemáticos básicos:

- `+` (Suma): Suma dos operandos.  
  Ejemplo: `5 + 3 = 8`

- `-` (Resta): Resta el segundo operando del primero.  
  Ejemplo: `5 - 3 = 2`

- `*` (Multiplicación): Multiplica dos operandos.  
  Ejemplo: `5 * 3 = 15`

- `/` (División): Divide el primer operando entre el segundo. Si ambos operandos son enteros, el resultado también será un entero. Si uno de los operandos es decimal, el resultado será decimal.  
  Ejemplo: `5 / 2 = 2` (división entera)  
           `5.0 / 2 = 2.5`

- `%` (Módulo o residuo): Devuelve el resto de la división entre dos operandos.  
  Ejemplo: `5 % 2 = 1`

#### 2. Precedencia de los Operadores Aritméticos:
La precedencia determina el orden en que se evaluan los operadores en una expresión. Los operadores con mayor precedencia se ejecutan primero.

| Operador    | Descripción                  | Precedencia |
|-------------|------------------------------|-------------|
| `*`, `/`, `%` | Multiplicación, división, módulo | 14          |
| `+`, `-`    | Suma, resta                   | 13          |

#### 3. Asociatividad de los Operadores Aritméticos:
Los operadores aritméticos tienen **asociatividad de izquierda a derecha**, lo que significa que los operadores de igual precedencia se evaluarán de izquierda a derecha.

**Ejemplo 1**:
- Expresión: `10 / 2 * 3`  
  Primero se evalúa la división: `10 / 2 = 5`, luego la multiplicación: `5 * 3 = 15`.

**Ejemplo 2**:
- Expresión: `10 - 3 + 2`  
  Se evalúa de izquierda a derecha:  
  Primero se evalúa la resta: `10 - 3 = 7`, luego la suma: `7 + 2 = 9`.

#### 4. Uso de Paréntesis para Modificar la Precedencia:
Los paréntesis tienen la **mayor precedencia** y pueden modificar el orden en que se evalúan las expresiones.

**Ejemplo**:
- Expresión: `5 + 3 * 2` (resultado: 11, porque primero se hace `3 * 2` y luego se suma `5`)
- Expresión con paréntesis: `(5 + 3) * 2` (resultado: 16, porque primero se suma `5 + 3` y luego se multiplica por `2`)

#### Resumen:
- **Precedencia**: Define el orden de evaluación de los operadores.
- **Asociatividad**: Los operadores aritméticos tienen asociatividad de izquierda a derecha.

---

### CONVERSIÓN DE TIPOS EN C#

#### 1. Conversión Implícita (Automática):
En algunos casos, el compilador realiza automáticamente la conversión entre tipos sin necesidad de intervención del programador. Esto ocurre cuando no hay pérdida de datos entre los tipos.

**Ejemplos**:
- De `int` a `float` o `double`:  
  `int numeroEntero = 10;`  
  `double numeroDecimal = numeroEntero;`  // Conversión implícita

- De `float` a `double`:  
  `float numeroFloat = 3.14f;`  
  `double numeroDouble = numeroFloat;`  // Conversión implícita

#### 2. Conversión Explícita (Type Casting):
Cuando el compilador no puede realizar la conversión automáticamente, se debe usar un **type cast** explícito.

**Ejemplos**:
- De `double` a `int` (puede perder la parte decimal):  
  `double numeroDecimal = 9.78;`  
  `int numeroEntero = (int)numeroDecimal;`  // Conversión explícita

- De `float` a `int` (pierde la parte decimal):  
  `float numeroFloat = 3.99f;`  
  `int numeroEntero = (int)numeroFloat;`  // Conversión explícita

#### 3. Conversión Usando Métodos de Conversión Estática (Convert):
La clase `Convert` permite realizar conversiones entre varios tipos de manera segura.

**Ejemplo**:  
  `double numeroDecimal = 9.78;`  
  `int numeroEntero = Convert.ToInt32(numeroDecimal);`  // Convertir de double a int

**Métodos comunes**:
- `Convert.ToInt32()`
- `Convert.ToDouble()`
- `Convert.ToString()`
- `Convert.ToBoolean()`

**Ejemplo de conversión de `string` a `int`**:  
  `string texto = "123";`  
  `int numero = Convert.ToInt32(texto);`  // Convierte un string a int

#### 4. Métodos de Parseo (Parse):
La función `Parse` también convierte entre tipos, pero puede lanzar excepciones si el valor no es convertible.

**Ejemplo**:  
  `string texto = "456";`  
  `int numero = int.Parse(texto);`  // Convierte un string a int

**Excepciones comunes**:
- Si el string no puede convertirse en el tipo deseado, lanzará una excepción `FormatException`.

#### Uso de TryParse (para evitar excepciones):
  `string texto = "789";`  
  `int numero;`  
  `bool exito = int.TryParse(texto, out numero);`  // Devuelve 'true' si la conversión es exitosa

#### 5. Conversión entre Tipos Personalizados (Clase o Estructura):
Puedes definir conversiones personalizadas entre tipos en tus propias clases o estructuras usando los operadores de conversión.

**Ejemplo**:
  ```csharp
  public class Punto
  {
      public int X { get; set; }
      public int Y { get; set; }

      // Conversión explícita de Punto a tupla
      public static explicit operator (int, int)(Punto p)
      {
          return (p.X, p.Y);
      }
  }

  Punto p = new Punto { X = 10, Y = 20 };
  var tupla = (ValueTuple<int, int>)p;  // Conversión explícita
  ```

#### Resumen de Conversión de Tipos:

| Tipo de Conversión        | Descripción                                | Ejemplo                |
|---------------------------|--------------------------------------------|------------------------|
| Implícita (Automática)      | El compilador realiza la conversión sin intervención. | `int -> double`        |
| Explícita (Type Casting)    | Se usa `(tipo)valor` para realizar la conversión, con posible pérdida de datos. | `double -> int`        |
| Método Convert              | Uso de la clase `Convert` para una conversión más segura y controlada. | `Convert.ToInt32()`    |
| Parse                       | Usa `int.Parse()` o `double.Parse()` para convertir un `string` en un número. | `int.Parse()`          |
| TryParse                    | Evita excepciones con `TryParse()` al intentar convertir un `string`. | `int.TryParse()`       |
| Conversión Personalizada    | Definir conversiones explícitas entre tipos personalizados usando operadores. | `(Punto -> (int, int))`|

---

## OBTENCION DE TIPOS EN C#

// Obtener el tipo de dato de las variables
```csharp
Type tipoPosicion1 = posicionInt1.GetType();  // Tipo: System.Int32
Type tipoCalorias1 = caloriasFlt1.GetType();  // Tipo: System.Single (float)
Type tipoPeso1 = pesoStr1.GetType();          // Tipo: System.String
Type tipoAltitud1 = altitudStr1.GetType();    // Tipo: System.String

Type tipoPosicion2 = posicionInt2.GetType();  // Tipo: System.Int32
Type tipoCalorias2 = caloriasFlt2.GetType();  // Tipo: System.Single (float)
Type tipoPeso2 = pesoStr2.GetType();          // Tipo: System.String
Type tipoAltitud2 = altitudStr2.GetType();    // Tipo: System.String
```


## LISTAS
#### TIPOS DE DATOS
```
    using System.Collections.Generic;

    List<int> numeros = new List<int>();  // Lista de enteros
    List<string> nombres = new List<string>();  // Lista de cadenas
```
#### AÑADIR ELEMENTOS A LA LISTA
```
    numeros.Add(10);
    numeros.Add(20);
    numeros.Add(30);
```

#### AÑADIR VARIOS ELEMENTOS DEL TIRON A LA LISTA
```
    numeros.AddRange(new int[] { 40, 50, 60 });

```

#### INSERTAR EN UNA POSICIÓN ESPECIFICA
```
    numeros.Insert(1, 15);  // Inserta el número 15 en el índice 1
```

#### ACCESO A LOS ELEMENTOS
```
    Console.WriteLine(numeros[0]);  // Salida: 10
    Console.WriteLine(numeros[2]);  // Salida: 30
```
#### TAMAÑO DE LA LISTA
```
    Console.WriteLine(numeros.Count);  // Salida: 3
```
#### REVERSE
```
            lista.Reverse();
```

#### ELIMINAR UN ELEMENTO
Elimina la primera aparición de un valor en la lista.
```
    numeros.Remove(20);  // Elimina el número 20 de la lista
```

#### ELIMINAR ELEMENTO DE UNA POSICION ESPECIFICA
```
    numeros.RemoveAt(0);  // Elimina el primer elemento de la lista

```

#### BUSCAR UN ELEMENTO
Devuelve true si un elemento está presente en la lista, de lo contrario false.

```
    if (numeros.Contains(30))
    {
        Console.WriteLine("El número 30 está en la lista.");
    }

```

#### ORDENAR ELEMENTOS

```
    numeros.Sort();
```

#### LIMPIAR LA LISTA

```
    numeros.Clear();
```

#### CONVERTIR UNA LISTA DE STRING A INT

```
    List<int> listaEnteros = listaStrings.ConvertAll(int.Parse);
```



## OPERACIONES BÁSICAS CON CADENAS DE TEXTO (strings)
```
    string a = "GNU/";
    string b = "Linux";
    string c = a + b;  // Concatenación. Resultado: "GNU/Linux"
```

## FUNCIONES MATEMATICAS
```
  Math.PI (Importa pi)
  Math.Pow(numero a elevar, numero elevado)
```










