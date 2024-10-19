@tool
extends EditorScript

# Elimina todas las vocales dada una cadena, o string, de cinco caracteres.
# @author Victor Fernandez España

func _run() -> void:
	var cadena = "Hola!"
	var vocales = "AEIOUaeiouáéíóúÁÉÍÓÚ"
	
	if cadena.length() != 5:
		print("Tiene que tener 5 caracteres.")
	else:
		if cadena[0] in vocales:
			cadena = cadena.replace(cadena[0], "")
		if cadena[1] in vocales:
			cadena = cadena.replace(cadena[1], "")
		if cadena[2] in vocales:
			cadena = cadena.replace(cadena[2], "")
		if cadena[3] in vocales:
			cadena = cadena.replace(cadena[3], "")
		if cadena[4] in vocales:
			cadena = cadena.replace(cadena[4], "")

		print("Cadena sin vocales: %s" % cadena)
