@tool
extends EditorScript

# Crea un programa que determine si un número entero es par o impar (pista: usar la operación %).
# @author Victor Fernandez España

func _run() -> void:
	var a = 3
	if a % 2 == 0:
		print("Es par")
	else:
		print("Es impar")
