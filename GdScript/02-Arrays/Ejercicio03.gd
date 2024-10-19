
@tool
extends EditorScript
# Crea un array/lista con cinco elementos de tipo número real y multiplica todos sus elementos e imprime el resultado por pantalla.
# @author Victor Fernandez España

func _run() -> void:
	var array: Array = [1.0, 2.0, 3.0, 4.0, 5.0]
	var multiplicacion: float = array[0] * array[1] * array[2] * array[3] * array[4]

	print("La multiplicación es: ", multiplicacion)
