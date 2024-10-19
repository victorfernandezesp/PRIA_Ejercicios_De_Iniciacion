
@tool
extends EditorScript
# Multiplica tres enteros, concatena el resultado con un 4 al final y divide el resultado por 2.
# @author Victor Fernandez España

func _run() -> void:
	var numero1: int = -2
	var numero2: int = -1
	var numero3: int = 3

	var multiplicacion: int = numero1 * numero2 * numero3
	var concatenacion: String = str(multiplicacion) + "4"
	var division: int = int(concatenacion) / 2  

	print("Multiplicación: ", multiplicacion)
	print("Concatenación: ", concatenacion)
	print("División: ", division)
