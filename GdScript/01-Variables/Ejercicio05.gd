
@tool
extends EditorScript
# Inicializa cuatro variables de diferentes tipos y las imprime en un mismo mensaje.
# @author Victor Fernandez España

func _run() -> void:
	var var1: int = 10          
	var var2: String = "20"     
	var var3: float = 30.50     
	var var4: bool = true       

	print(var1, "\n", var2, "\n", var3, "\n", var4, "\n")
