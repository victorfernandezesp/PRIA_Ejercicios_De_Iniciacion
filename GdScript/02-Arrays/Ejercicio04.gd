
@tool
extends EditorScript
# Crea un array/lista con cinco elementos y elimina el primer, tercer y último elemento. Por último, imprime de nuevo el array o lista.
# @author Victor Fernandez España

func _run() -> void:
	var array: Array = [1, 2, 3, 4, 5]
	array.remove_at(4)
	array.remove_at(2)
	array.remove_at(0)

	print("El array final es: ", array)
