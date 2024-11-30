@tool
extends EditorScript

class_name Rectangulo

var longitud: float
var ancho: float

func _init(longitud = 0, ancho = 0):
	self.longitud = longitud
	self.ancho = ancho

func area() -> float:
	return longitud * ancho

func _run():
	var rectangulo1 = Rectangulo.new(10, 20)
	print("Área del rectángulo 1:", rectangulo1.area()) 

	var rectangulo2 = Rectangulo.new(30, 40)
	print("Área del rectángulo 2:", rectangulo2.area()) 

	var rectangulo3 = Rectangulo.new(50, 60)
	print("Área del rectángulo 3:", rectangulo3.area()) 
