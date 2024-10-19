@tool
extends EditorScript

# Crea un programa que determine si una letra es vocal o consonante.
# @author Victor Fernandez España

func _run() -> void:
	var vocal = "AEIOUaeiouáéíóúÁÉÍÓÚ"
	var letra = "e"
	
	if letra in vocal:
		print("Es Vocal")
	else:
		print("Es Consonante")
