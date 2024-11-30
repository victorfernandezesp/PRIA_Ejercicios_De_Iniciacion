@tool
extends EditorScript

class_name Linea

var x1: float
var y1: float
var x2: float
var y2: float

func _init(x1 = 0, y1 = 0, x2 = 0, y2 = 0):
	self.x1 = x1
	self.y1 = y1
	self.x2 = x2
	self.y2 = y2

func punto_medio() -> Vector2:
	return Vector2((x1 + x2) / 2, (y1 + y2) / 2)

func _run():
	var linea1 = Linea.new(10, 20, 30, 40)
	print("Punto medio de linea1:", linea1.punto_medio()) 

	var linea2 = Linea.new(50, 60, 70, 80)
	print("Punto medio de linea2:", linea2.punto_medio())  

	var linea3 = Linea.new(90, 100, 110, 120)
	print("Punto medio de linea3:", linea3.punto_medio())  
