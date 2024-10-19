
@tool
extends EditorScript
# Imprime GNU si el número recibido es impar.
# @author Victor Fernandez España

func _run() -> void:
	var numero1: int = 3
	var parimpar1: int = numero1 % 2
	
	print("GNU" if parimpar1 == 1 else "")
