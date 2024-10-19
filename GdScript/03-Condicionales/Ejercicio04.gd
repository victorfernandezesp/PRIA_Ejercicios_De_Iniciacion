@tool
extends EditorScript

# Crear un programa que determine si un número es menor que 0, o que está entre 0 y 50, o entre 51 y 100 o por encima de 100.
# @author Victor Fernandez España

func _run() -> void:
	var a = 56
	if a < 0:
		print("Es menor que 0")
	elif a <= 50:
		print("Está entre 0 y 50")
	elif a <= 100:
		print("Está entre 51 y 100")
	else:
		print("Es mayor a 100")
