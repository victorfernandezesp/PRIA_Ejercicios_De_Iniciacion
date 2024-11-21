extends Node

func maximo(num1, num2):
	return num1 if num1 > num2 else num2

func _ready():
	print(maximo(4, 5))
	print(maximo(5, 4))
	print(maximo(6, 6))
