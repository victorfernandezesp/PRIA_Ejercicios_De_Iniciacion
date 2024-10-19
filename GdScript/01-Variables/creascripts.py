# Script para crear 20 archivos GDScript con contenido dado

# Función para crear un archivo GDScript
def crear_archivo_gdscript(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"Archivo {nombre_archivo} creado con éxito.")

# Código GDScript a insertar en los archivos
codigo_gdscript = """
@tool
extends EditorScript

func _run() -> void:
    print("Hola, Mundo")
"""

# Crear 20 archivos con nombres secuenciales Ejercicio01.gd, Ejercicio02.gd, ...
for i in range(1, 21):
    nombre_archivo = f"Ejercicio{i:02}.gd"  # Formato para tener siempre dos dígitos
    crear_archivo_gdscript(nombre_archivo, codigo_gdscript)
