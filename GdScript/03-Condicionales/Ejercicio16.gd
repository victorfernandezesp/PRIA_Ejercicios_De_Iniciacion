@tool
extends EditorScript

# Dadas dos series de tres enteros, comprueba si todos los enteros de la primera serie aparecen en alguno de los enteros de la segunda serie.
# @author Victor Fernandez España

func _run() -> void:
	var entero1 = 1
	var entero2 = 2
	var entero3 = 3
	var entero4 = 2
	var entero5 = 3
	var entero6 = 4
	
	var primero_en_segunda = entero1 == entero4 or entero1 == entero5 or entero1 == entero6
	var segundo_en_segunda = entero2 == entero4 or entero2 == entero5 or entero2 == entero6
	var tercero_en_segunda = entero3 == entero4 or entero3 == entero5 or entero3 == entero6
	
	if primero_en_segunda and segundo_en_segunda and tercero_en_segunda:
		print("Sí.")
	else:
		print("No.")
