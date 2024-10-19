
@tool
extends EditorScript
# Inicializa una variable fahrenheit, calcula su equivalente a grados Celsius e imprime el resultado.
# Fórmula: celsius = (fahrenheit - 32) / 1.8.
# @author Victor Fernandez España

func _run() -> void:
	var fahrenheit: float = 33.0
	var celsius: float = (fahrenheit - 32) / 1.8
	print(celsius)
