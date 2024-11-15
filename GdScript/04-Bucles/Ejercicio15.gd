
@tool
extends EditorScript

#        15. Muestra la suma de los dígitos de 2n, siendo n un número natural.

# 			Autor: Victor Fernandez España


func _run() -> void:

	var n = 12

	var valor = str(pow(2, n))
	var acumulador = 0

	for i in valor:
		acumulador += int(i)

	print(acumulador)
