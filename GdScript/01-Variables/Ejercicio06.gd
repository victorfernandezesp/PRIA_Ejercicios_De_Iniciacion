
@tool
extends EditorScript
# Inicializa una variable radio y calcula la circunferencia.
# Fórmula: 2 · π · radio.
# @author Victor Fernandez España

func _run() -> void:
	var radio: float = 10.0
	var circunferencia: float = 2 * PI * radio
	print(circunferencia)
