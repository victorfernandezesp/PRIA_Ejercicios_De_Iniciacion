@tool
extends EditorScript

# Calcula el ángulo que forman dos vectores 2D.
# Autor: Victor Fernandez España
class_name Punto

var x: float
var y: float

func init(x: float, y: float):
	self.x = x
	self.y = y

static func angulo(vector1: Punto, vector2: Punto) -> float:
	return (atan2(vector2.y, vector2.x) - atan2(vector1.y, vector1.x)) * 180 / PI

func _run():
	var vector1 = Punto.new()
	vector1.init(5.45, 1.12)
	
	var vector2 = Punto.new()
	vector2.init(-3.86, 4.32)
	
	var resultado = Punto.angulo(vector1, vector2)
	print("El ángulo entre los vectores es: ", resultado, " grados")
