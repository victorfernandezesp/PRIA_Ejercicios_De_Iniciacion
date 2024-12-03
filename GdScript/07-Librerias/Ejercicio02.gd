@tool
extends Node

# Autor: Victor Fernandez España

func _ready():
	# Ejemplo 1: Uso de la librería Math (Cálculo del valor absoluto)
	var numero = -5
	var valor_absoluto = abs(numero)
	print("El valor absoluto de ", numero, " es: ", valor_absoluto)
	
	# Ejemplo 2: Uso de la librería OS (Obtener información del sistema operativo)
	var sistema_operativo = OS.get_name()
	print("El sistema operativo es: ", sistema_operativo)
	
	# Ejemplo 3: Uso de la librería Vector2 (Operaciones con vectores 2D)
	var vector1 = Vector2(5, 3)
	var vector2 = Vector2(2, 7)
	
	var suma = vector1 + vector2
	var producto_punto = vector1.dot(vector2)
	
	print("La suma de los vectores es: ", suma)
	print("El producto punto de los vectores es: ", producto_punto)
