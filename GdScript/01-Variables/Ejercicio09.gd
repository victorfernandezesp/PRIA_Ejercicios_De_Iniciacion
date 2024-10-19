
@tool
extends EditorScript
# Inicializa una variable celsius, calcula su equivalente a grados Fahrenheit e imprime el resultado.
# Fórmula: fahrenheit = (celsius * 1.8) + 32.
# @author Victor Fernandez España

func _run() -> void:
	var celsius: float = 33.0
	var fahrenheit: float = (celsius * 1.8) + 32
	print(fahrenheit)
