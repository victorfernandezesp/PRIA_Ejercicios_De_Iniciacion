
@tool
extends EditorScript
# 15. Dada una serie de palabras, ordénalas alfabéticamente.
# @author Victor Fernandez España
func _run() -> void:
	var array: Array

	array = []
	array.append("perro")
	array.append("gato")
	array.append("camaleón")
	array.append("toro")
	array.append("puma")

	array.sort()
	print(array)
