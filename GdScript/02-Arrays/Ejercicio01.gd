
@tool
extends EditorScript
# Crea un array o una lista con cinco elementos e imprime en pantalla el primer, tercer y último elemento.
# @author Victor Fernandez España

func _run() -> void:
	var array: Array = [1, 2, 3, 4, 5]
	print("Primer elemento: ", array[0])
	print("Tercer elemento: ", array[2])
	print("Último elemento: ", array[4])
