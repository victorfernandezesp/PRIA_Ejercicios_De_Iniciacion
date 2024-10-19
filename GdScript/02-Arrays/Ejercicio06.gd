
@tool
extends EditorScript
# Convierte un array/lista de números que sean de tipo cadena de caracteres a tipo número real.
# @author Victor Fernandez España

func _run() -> void:
	var array: Array = ["1", "2", "3", "4", "5"]
	array[0] = float(array[0])
	array[1] = float(array[1])
	array[2] = float(array[2])
	array[3] = float(array[3])
	array[4] = float(array[4])
	print("El array final es: ", array)
