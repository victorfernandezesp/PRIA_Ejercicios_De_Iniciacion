@tool
extends EditorScript

# 12. En un array 3x3 de enteros, muestra la suma más alta de los números de una fila.
# @author Victor Fernandez España

func _run() -> void:
	var array = [
		[], 
		[], 
		[]
	]

	var numero1 = 6
	var numero2 = 8
	var numero3 = 1
	var numero4 = 3
	var numero5 = 5
	var numero6 = 6
	var numero7 = 3
	var numero8 = 2
	var numero9 = 1

	array[0].append(numero1)
	array[0].append(numero2)
	array[0].append(numero3)
	array[1].append(numero4)
	array[1].append(numero5)
	array[1].append(numero6)
	array[2].append(numero7)
	array[2].append(numero8)
	array[2].append(numero9)

	var suma_fila1 = array[0][0] + array[0][1] + array[0][2]
	var suma_fila2 = array[1][0] + array[1][1] + array[1][2]
	var suma_fila3 = array[2][0] + array[2][1] + array[2][2]
	var suma_maxima = max(suma_fila1, suma_fila2, suma_fila3)
	print(suma_maxima)
