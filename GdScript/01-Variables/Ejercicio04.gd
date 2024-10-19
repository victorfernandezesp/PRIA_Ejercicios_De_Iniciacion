
@tool
extends EditorScript
# Inicializa dos variables de tipo número entero, suma las variables e imprime el resultado.
# @author Victor Fernandez España

func _run() -> void:
	var numero1: int = 20
	var numero2: int = 10
	var resultado: int = numero1 + numero2
	print("Número ", numero1, " + ", numero2, " = ", resultado)
