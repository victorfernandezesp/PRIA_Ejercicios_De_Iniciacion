
@tool
extends EditorScript

# Crea un array/lista de números de tipo número real, ordénalos e imprime dicho array, o lista, por pantalla.
# @author Victor Fernandez España

func _run() -> void:
	var array: Array = [1, 3, 5, 4, 2]
	print("El array sin ordenar:   ", array)
	array.sort()
	print("El array ordenado:      ", array)
