
@tool
extends EditorScript
# Crea un array/lista de números de tipo cadena de caracteres, ordénalos e imprime dicho array, o lista, por pantalla.
# @author Victor Fernandez España

func _run() -> void:
	var array: Array = ["5", "2", "1", "4", "3"]
	print("El array sin ordenar:   ", array)
	array.sort()
	print("El array ordenado:      ", array)
