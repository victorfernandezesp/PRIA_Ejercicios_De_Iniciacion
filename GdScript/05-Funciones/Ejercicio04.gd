extends Node

func listador(num1: int, num2: int) -> Array:
	var array = []
	array.append(num1)
	array.append(num2)
	array.append((num1 + num2) / 2)
	array.sort()
	return array

func _ready():
	print(listador(4, 5))
	print(listador(5, 4))
	print(listador(6, 6))
