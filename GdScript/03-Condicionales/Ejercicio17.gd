@tool
extends EditorScript

# Convierte de centímetros a metros y viceversa.
# @author Victor Fernandez España

func _run() -> void:
	var numero1 = 150.0
	var medida2 = "cm"
	
	var medidas = ["cm", "m"]
	
	if medida2 not in medidas:
		print("La medida introducida no es correcta.")
	else:
		if medida2 == medidas[0]:
			numero1 *= 0.01
			print("La conversión da: %sm" % numero1)
		else:
			numero1 *= 100
			print("La conversión da: %scm" % numero1)
