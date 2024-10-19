
@tool
extends EditorScript
# Convierte una variable de tipo cadena a número real, réstale 21.34 e imprime el resultado.
# @author Victor Fernandez España

func _run() -> void:
	var latitud: String = "-234.62"
	var numeroReal: float = float(latitud)  
	numeroReal -= 21.34                     
	print(numeroReal)                       
