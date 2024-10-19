@tool
extends EditorScript

# Dado dos enteros, calcula la suma. Si el resultado está entre 10 y 19 (ambos incluídos), imprime 20. Si no, imprime la suma.
# @author Victor Fernandez España

func _run() -> void:
	var entero1 = 6
	var entero2 = 8
	
	var resultado = entero1 + entero2
	
	if resultado >= 10 and resultado <= 19:
		print("20.")
	else:
		print("%d." % resultado)
