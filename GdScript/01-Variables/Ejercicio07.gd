
@tool
extends EditorScript
# Inicializa una variable radio y calcula el área de un círculo.
# Fórmula: π · radio · radio.
# @author Victor Fernandez España

func _run() -> void:
	var radio: float = 10.0
	var area: float = PI * radio * radio
	print(area)
