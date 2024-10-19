@tool
extends EditorScript
# 16. Dada una serie de palabras, ordénalas alfabéticamente al revés (de z a a). A continuación, muestra el resultado final exceptuando la primera palabra y las tres últimas palabras.
# @author Victor Fernandez España
func _run() -> void:
	var array = []
	var palabra = "agua"
	array.append(palabra)
	palabra = "mano"
	array.append(palabra)
	palabra = "cielo"
	array.append(palabra)
	palabra = "tarde"
	array.append(palabra)
	palabra = "verano"
	array.append(palabra)
	palabra = "invierno"
	array.append(palabra)
	array.sort()
	array.reverse()
	array.pop_front()
	array.pop_back()
	array.pop_back()
	array.pop_back()
	print(array)
