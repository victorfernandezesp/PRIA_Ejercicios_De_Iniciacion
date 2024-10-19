@tool
extends EditorScript

# Crea un programa que imprima por orden alfabético tres cadena de caracteres o strings dados y que imprima si son o no iguales dichos tres strings.
# @author Victor Fernandez España

func _run() -> void:
	var cadena1 = "Hola"
	var cadena2 = "Holaa"
	var cadena3 = "Holaaa"
	
	var arrayOrden = [cadena1, cadena2, cadena3]
	arrayOrden.sort() 
	
	print("Ordenado: %s" % arrayOrden)

	if cadena1 == cadena2 and cadena1 == cadena3:
		print("Las cadenas SON iguales.")
	else:
		print("Las cadenas NO son iguales.")
