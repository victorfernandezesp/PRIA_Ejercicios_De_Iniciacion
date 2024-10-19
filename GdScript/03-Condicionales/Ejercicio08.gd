@tool
extends EditorScript

# Crea un programa que encuentre el número mayor a partir de tres números dados.
# @author Victor Fernandez España

func _run() -> void:
	var numero1 = 60
	var numero2 = 60
	var numero3 = 40
	
	if numero1 > numero2 and numero1 > numero3:
		print("%d es el mayor." % numero1)
	elif numero2 > numero1 and numero2 > numero3:
		print("%d es el mayor." % numero2)
	else:
		print("%d es el mayor." % numero3)
