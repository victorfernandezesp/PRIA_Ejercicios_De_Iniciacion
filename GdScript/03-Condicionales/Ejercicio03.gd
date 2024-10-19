@tool
extends EditorScript

# Crea un programa que determine si una variable de tipo numérico es positiva, negativa o cero.
# @author Victor Fernandez España

func _run() -> void:
	var a = -2
	if a > 0:
		print("Es mayor que 0")
	elif a < 0:
		print("Es menor que 0")
	else:
		print("Es igual a 0")
