@tool
extends EditorScript

# Detecta la primera aparición de un entero a partir de una serie de cinco enteros devolviendo el índice con su posición.
# @author Victor Fernandez España

func _run() -> void:
	var entero1 = 3
	var entero2 = 1
	var entero3 = 2
	var entero4 = 3
	var entero5 = 4
	var entero6 = 5
	
	var array = [entero2, entero3, entero4, entero5, entero6]
	
	if entero1 == array[0]:
		print("1")
	elif entero1 == array[1]:
		print("2")
	elif entero1 == array[2]:
		print("3")
	elif entero1 == array[3]:
		print("4")
	elif entero1 == array[4]:
		print("5")
	else:
		print("No está el número.")
