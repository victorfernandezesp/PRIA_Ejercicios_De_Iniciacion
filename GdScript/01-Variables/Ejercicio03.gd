@tool
extends EditorScript
# Inicializa dos variables edad y altura e imprímelas en un mensaje.
# @author Victor Fernandez España

func _run() -> void:
	var edad: int = 20
	var altura: int = 183
	print("Tengo %d años y mido %d cm" % [edad, altura])
