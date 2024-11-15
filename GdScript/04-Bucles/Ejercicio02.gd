
@tool
extends EditorScript

#         2. Genera una tabla de multiplicar, del 1 al 10, de un número entero dado.
# 			Autor: Victor Fernandez España


func _run() -> void:

	var numero = 5

	for i in range(10):
		print(str(numero) + " * " + str(i) + " = " + str(numero * i))
