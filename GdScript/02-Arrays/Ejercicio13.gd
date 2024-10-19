@tool
extends EditorScript

# 13. Muestra la fila de una matriz 3x3 de enteros cuya suma de números sea la más alta.
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

	var mayor_suma = suma_fila1
	var fila_mayor = array[0]

	mayor_suma = suma_fila2 if suma_fila2 > mayor_suma else mayor_suma
	fila_mayor = array[1] if suma_fila2 > mayor_suma else fila_mayor

	mayor_suma = suma_fila3 if suma_fila3 > mayor_suma else mayor_suma
	fila_mayor = array[2] if suma_fila3 > mayor_suma else fila_mayor

	print(fila_mayor)
