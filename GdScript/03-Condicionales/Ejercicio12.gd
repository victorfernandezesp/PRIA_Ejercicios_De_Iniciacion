@tool
extends EditorScript

# Dado tres enteros, devuelve verdadero si no aparece ni un 1 y ni un 3.
# @author Victor Fernandez España

func _run() -> void:
	var entero1 = 6
	var entero2 = 2
	var entero3 = 4
	
	var noAparecen = [1, 3]
	
	if entero1 not in noAparecen and entero2 not in noAparecen and entero3 not in noAparecen:
		print("True")
	else:
		print("False")
