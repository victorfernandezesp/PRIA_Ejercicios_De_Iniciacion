
@tool
extends EditorScript
# Calcula el área y el perímetro de un rectángulo dado sus lados.
# @author Victor Fernandez España

func _run() -> void:
	var numero1: float = 3.0  
	var numero2: float = 2.0 

	var area: float = numero1 * numero2
	var perimetro: float = (numero1 * 2) + (numero2 * 2)

	print("Área: ", area)
	print("Perímetro: ", perimetro)
