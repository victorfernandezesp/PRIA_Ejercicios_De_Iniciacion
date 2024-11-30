@tool
extends EditorScript

class_name Punto

var x: int
var y: int

func _init(x = 0, y = 0):
	self.x = x
	self.y = y


func getX() -> int:
	return self.x

func getY() -> int:
	return self.y

func setX(x):
	self.x = x

func setY(y):
	self.y = y

func _run():
	var punto1 = Punto.new(10, 20)
	print(punto1.getX()) 
	print(punto1.getY()) 
	punto1.setX(30)
	punto1.setY(40)
	print(punto1.getX()) 
	print(punto1.getY()) 

	var punto2 = Punto.new(50, 60)
	print(punto2.getX()) 
	print(punto2.getY()) 
	punto2.setX(70)
	punto2.setY(80)
	print(punto2.getX()) 
	print(punto2.getY()) 

	var punto3 = Punto.new(90, 100)
	print(punto3.getX())  
	print(punto3.getY())  
	punto3.setX(110)
	punto3.setY(120)
	print(punto3.getX())  
	print(punto3.getY())  
