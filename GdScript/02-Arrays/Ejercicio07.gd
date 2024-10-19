
@tool
extends EditorScript
# Crea un array/lista e imprime en pantalla el número de elementos.
# @author Victor Fernandez España

func _run() -> void:
	var array: Array = ["1", "2", "3", "4", "5"]

	print("El número de elementos del array es: ", array.size())
