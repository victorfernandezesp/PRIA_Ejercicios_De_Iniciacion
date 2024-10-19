
@tool
extends EditorScript
# Dado tres enteros, súmalos e imprime el resultado.
# @author Victor Fernandez España

func _run() -> void:
	var numero1: int = 3
	var numero2: int = 7
	var numero3: int = 5

	var suma: int = numero1 + numero2 + numero3
	print(numero1, "+", numero2, "+", numero3, "=", suma)
