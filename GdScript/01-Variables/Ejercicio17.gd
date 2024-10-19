
@tool
extends EditorScript
# Dados cinco enteros, indica con un 0 si el número es par y con un 1 si el número es impar.
# @author Victor Fernandez España

func _run() -> void:
	var numero1: int = 2
	var parimpar1: int = numero1 % 2

	var numero2: int = 25
	var parimpar2: int = numero2 % 2

	var numero3: int = 34
	var parimpar3: int = numero3 % 2

	var numero4: int = 22
	var parimpar4: int = numero4 % 2

	var numero5: int = 13
	var parimpar5: int = numero5 % 2

	print("Resultado: ", parimpar1, " ", parimpar2, " ", parimpar3, " ", parimpar4, " ", parimpar5)
