
@tool
extends EditorScript
# Crea un array/lista de números de tipo número real, ordénalos al revés e imprime dicho array, o lista, por pantalla.
# @author Victor Fernandez España

func _run() -> void:
	var array: Array = [1, 2, 3, 4, 5]
	print("El array sin ordenar:   ", array)
	array.sort()
	array.reverse()
	print("El array ordenado:      ", array)
