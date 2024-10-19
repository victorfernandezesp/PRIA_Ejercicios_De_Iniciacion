@tool
extends EditorScript

# Dado cinco enteros, devuelve verdadero si aparece alguna vez 3 enteros impares consecutivos.
# @author Victor Fernandez España

func _run() -> void:
	var entero1 = 1
	var entero2 = 3
	var entero3 = 5
	var entero4 = 2
	var entero5 = 7
	
	var esImPar1 = entero1 % 2 == 1
	var esImPar2 = entero2 % 2 == 1
	var esImPar3 = entero3 % 2 == 1
	var esImPar4 = entero4 % 2 == 1
	var esImPar5 = entero5 % 2 == 1
	
	if esImPar1 and esImPar2 and esImPar3:
		print("True")
	elif esImPar2 and esImPar3 and esImPar4:
		print("True")
	elif esImPar3 and esImPar4 and esImPar5:
		print("True")
	else:
		print("False")
