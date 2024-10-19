@tool
extends EditorScript

# Crea un programa que determine si, dado sus tres ángulos, se puede formar un triángulo (pista: un triángulo se forma cuando sus tres ángulos suman 180º).
# @author Victor Fernandez España

func _run() -> void:
	var angulo1 = 55
	var angulo2 = 100
	var angulo3 = 60
	
	if (angulo1 + angulo2 + angulo3) == 180:
		print("Es Triángulo")
	else:
		print("No es triángulo")
