@tool
extends EditorScript

class_name Circulo

var radio: float

func _init(radio = 0):
	self.radio = radio

func area() -> float:
	return PI * radio * radio

func circunferencia() -> float:
	return 2 * PI * radio

func _run():
	var circulo1 = Circulo.new(10)
	print("Área del círculo 1:", circulo1.area()) 
	print("Circunferencia del círculo 1:", circulo1.circunferencia())

	var circulo2 = Circulo.new(20)
	print("Área del círculo 2:", circulo2.area()) 
	print("Circunferencia del círculo 2:", circulo2.circunferencia()) 

	var circulo3 = Circulo.new(30)
	print("Área del círculo 3:", circulo3.area()) 
	print("Circunferencia del círculo 3:", circulo3.circunferencia()) 
