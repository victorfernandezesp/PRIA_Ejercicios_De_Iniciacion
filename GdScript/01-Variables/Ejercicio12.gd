
@tool
extends EditorScript
# Realiza un conversor de Fahrenheit a Celsius.
# @author Victor Fernandez España

func _run() -> void:
	var numero1: float = 68.0
	var numero2: float = 13.0
	var numero3: float = -145.6

	print(numero1, "ºF = ", ((5.0 / 9.0) * (numero1 - 32)), "ºC")
	print(numero2, "ºF = ", ((5.0 / 9.0) * (numero2 - 32)), "ºC")
	print(numero3, "ºF = ", ((5.0 / 9.0) * (numero3 - 32)), "ºC")
