
@tool
extends EditorScript
# Dado un entero, indica con un 0 si el número es par y con un 1 si el número es impar.
# @author Victor Fernandez España

func _run() -> void:
	var numero1: int = 2
	var parimpar: int = numero1 % 2 
	
	print("Es: ", parimpar)
