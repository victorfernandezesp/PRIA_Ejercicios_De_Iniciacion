
@tool
extends EditorScript
# Concatena dos números, convierte el resultado a entero y súmale 5.
# @author Victor Fernandez España

func _run() -> void:   
	var numero1: String = "2"
	var numero2: String = "4"
	
	var concatenado: String = numero1 + numero2
	var resultado: int = int(concatenado) + 5

	print("Concatenado: ", concatenado)
	print("Concatenado, pasándolo a entero y sumando 5: ", resultado)
