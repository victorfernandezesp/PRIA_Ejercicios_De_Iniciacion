
@tool
extends EditorScript

#     1. Crea un programa que:
#	  Sume todos los elementos (de tipo numérico) de un array, o lista, mediante un bucle.
#	  Multiplique todos los elementos (de tipo numérico) de un array, o lista, mediante un bucle.

func _run() -> void:
	var array = [1, 2, 3, 4, 5]

	var acumulador = 0
	var acumulador2 = 1

	for i in array:
		acumulador += i

	for i in array:
		acumulador2 *= i

	print("Suma: ", acumulador)
	print("Multiplicacion: ", acumulador2)
