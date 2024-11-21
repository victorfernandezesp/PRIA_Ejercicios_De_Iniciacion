extends Node

func es_par(num):
	return num % 2 == 0

func _ready():
	print(es_par(4))
	print(es_par(5))
	print(es_par(6))
