
@tool
extends EditorScript
# A partir de 5 números, muestra aquellos que no sean el mayor ni el menor y ordenados de mayor a menor.
# @author Victor Fernandez España
func _run() -> void:
	var array: Array = []
	
	var numero1: int = 1
	var numero2: int = 2
	var numero3: int = 3
	var numero4: int = 4
	var numero5: int = 5
	
	array.append(numero1)
	array.append(numero2)
	array.append(numero3)
	array.append(numero4)
	array.append(numero5)
	
	print("Array sin modificar:       ", array)

	array.sort()
	array.pop_front()
	array.pop_back()
	array.reverse()

	print("Array modificado:       ", array)
