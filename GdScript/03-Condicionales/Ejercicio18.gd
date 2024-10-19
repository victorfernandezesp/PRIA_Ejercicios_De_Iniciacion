@tool
extends EditorScript

# Dados dos enteros positivos, imprime el valor más cercano a 21 sin sobrepasarse. Imprime 0 si los dos enteros son mayores que 21.
# @author Victor Fernandez España

func _run() -> void:
	var numero1 = 19
	var numero2 = 25
	
	var numeros = [numero1, numero2]

	if max(numeros) <= 21:
		print("%d" % max(numeros))
	elif min(numeros) <= 21:
		print("%d" % min(numeros))
	else:
		print("0")
