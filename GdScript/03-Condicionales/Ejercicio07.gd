@tool
extends EditorScript

# Crea un programa que determine a partir de dos números cuál es el mayor y cuál es el menor o que imprima que son iguales si así lo son.
# @author Victor Fernandez España

func _run() -> void:
	var numero1 = 60
	var numero2 = 50
	
	if numero1 == numero2:
		print("Son iguales")
	elif numero1 > numero2:
		print("%d es mayor que %d" % [numero1, numero2])
	else:
		print("%d es mayor que %d" % [numero2, numero1])
