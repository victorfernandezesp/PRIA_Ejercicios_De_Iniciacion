@tool
extends EditorScript

func _run() -> void:
	var array = []
	var numero = 6
	array.append(numero)
	numero = 8
	array.append(numero)
	numero = 1
	array.append(numero)
	numero = 3
	array.append(numero)
	numero = 5
	array.append(numero)

	array.sort()
	var medianaNum = array[array.size() / 2]
	print(medianaNum)
