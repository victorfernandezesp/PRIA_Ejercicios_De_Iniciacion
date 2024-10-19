@tool
extends EditorScript
# 14. Dado un número con más de 10 dígitos, suma los 3 primeros dígitos y los 3 últimos dígitos.
# @author Victor Fernandez España

func _run() -> void:
	var numero: String
	var array: Array
	var suma: int

	numero = "123456789012"  
	array = []

	for digit in numero:
		array.append(int(digit))

	suma = array[0] + array[1] + array[2] + array[array.size() - 1] + array[array.size() - 2] + array[array.size() - 3]

	print(suma)
