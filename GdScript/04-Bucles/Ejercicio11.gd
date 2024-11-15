
@tool
extends EditorScript

#    11. Dada una serie de enteros, súmalos e imprime el resultado.

# 			Autor: Victor Fernandez España


func _run() -> void:

	var numeros = [1, 2, 3, 4, 5]
	var resultado = 0

	for i in numeros:
		resultado += i

	print("El resultado de la suma es: " + str(resultado))
