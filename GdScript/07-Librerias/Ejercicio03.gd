@tool
extends Node

# Autor: Victor Fernandez España

func _ready():
	var ruta_texto1 = "res://07-Librerias/texto1.txt"
	var ruta_texto2 = "res://07-Librerias/texto2.txt"
	var ruta_texto3 = "res://07-Librerias/texto3.txt"
	
	var texto1 = FileAccess.open(ruta_texto1, FileAccess.READ)
	var texto2 = FileAccess.open(ruta_texto2, FileAccess.READ)
	var texto3 = FileAccess.open(ruta_texto3, FileAccess.WRITE)

	if texto1 != null and texto2 != null:
		var contenido1 = texto1.get_as_text()
		var contenido2 = texto2.get_as_text()
		
		var textos_concatenados = contenido1 + contenido2
		
		texto3.store_string(textos_concatenados)
		texto3.close()

		print("Se ha creado un nuevo fichero con el contenido de los dos ficheros anteriores.")
		
		texto3.open(ruta_texto3, FileAccess.READ)
		print("El contenido del nuevo fichero es el siguiente:")
	else:
		print("Error al abrir los archivos de texto.")
