
@tool
extends EditorScript

# Crea un programa que determine si dos variables de tipo numérico son iguales o no.
# @author Victor Fernandez España

func _run() -> void:
	var a = 6
	var b = 8
	if a == b:
		print("Son iguales")
	else:
		print("No son iguales")
