@tool
extends EditorScript

# Crea un programa que determine si una persona está en edad de trabajar.
# @author Victor Fernandez España

func _run() -> void:
	var edadPersona = 15
	
	if edadPersona >= 16 and edadPersona <= 65:
		print("Está en edad de trabajar.")
	else:
		print("No está en edad de trabajar.")
