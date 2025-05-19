extends CharacterBody2D
class_name Personaje

var velocidad := 75.0
var tiene_llave: bool = false

@onready var agente_nav := $NavigationAgent2D
@onready var sprite := $AnimatedSprite2D
@onready var escena_bala: PackedScene = preload("res://Assets/Characters/EnemyT1/bala.tscn")
@onready var capa_disparo := get_tree().current_scene
@onready var label_balas := $Node/Label
@onready var label_vida := $Node/Label2

@onready var label_gasofa := $Items/LabelGasofa
@onready var label_bateria := $Items/LabelBatt
@onready var label_key := $Items/LabelKey

@onready var sonido_disparo := $SonidoDisparo

var contador_gasofa := 0
var contador_bateria := 0

var max_balas := 8
var balas_restantes := max_balas
var recargando := false
var tiempo_recarga := 5.0  
var tiempo_recarga_actual := 0.0

func _ready() -> void:
	agente_nav.path_desired_distance = 2.0
	agente_nav.target_desired_distance = 2.0
	agente_nav.debug_enabled = false

func _unhandled_input(evento: InputEvent) -> void:
	if evento is InputEventMouseButton and evento.pressed:
		if evento.button_index == MOUSE_BUTTON_LEFT:
			var destino := get_global_mouse_position()
			definir_objetivo(destino)
		elif evento.button_index == MOUSE_BUTTON_RIGHT and not recargando:
			disparar(get_global_mouse_position())
			balas_restantes -= 1
			if balas_restantes == 0:
				iniciar_recarga()

func definir_objetivo(destino: Vector2) -> void:
	agente_nav.target_position = destino
	cambiar_animacion(destino)

func cambiar_animacion(destino: Vector2) -> void:
	if destino.x < global_position.x:
		sprite.play("izquierda")
	else:
		sprite.play("default")

func disparar(destino: Vector2) -> void:
	cambiar_animacion(destino)

	var bala: Area2D = escena_bala.instantiate()
	bala.set_collision_layer_value(2, true)
	bala.set_collision_mask_value(1, true)
	bala.monitoring = true
	bala.monitorable = true

	bala.global_position = global_position
	bala.iniciar(destino - global_position)
	capa_disparo.add_child(bala)

	sonido_disparo.play()

func iniciar_recarga() -> void:
	recargando = true
	tiempo_recarga_actual = tiempo_recarga

func _process(delta: float) -> void:
	label_vida.text = str(GameManager.player_health)
	if recargando:
		tiempo_recarga_actual -= delta
		var segundos := int(tiempo_recarga_actual)
		var milisegundos := int((tiempo_recarga_actual - segundos) * 100)
		label_balas.text = str(segundos) + "." + str(milisegundos).pad_zeros(2) + "'' "
		if tiempo_recarga_actual <= 0.0:
			recargando = false
			balas_restantes = max_balas
			print("Recarga completada, balas disponibles:", balas_restantes)
	else:
		label_balas.text = str(balas_restantes)

func _physics_process(_delta: float) -> void:
	if agente_nav.is_navigation_finished():
		velocity = Vector2.ZERO
		return

	var posicion_actual: Vector2 = global_position
	var proxima_posicion: Vector2 = agente_nav.get_next_path_position()

	velocity = posicion_actual.direction_to(proxima_posicion) * velocidad
	move_and_slide()

func take_damage(damage: int) -> void:
	GameManager.player_health -= damage
	if GameManager.player_health <= 0:
		GameManager.reset_items()
		GameManager.player_health = 100
		get_tree().change_scene_to_file("res://Assets/Scenes/game_over.tscn")

		print("El personaje ha muerto")
	else:
		print("El personaje ha recibido daño. Salud restante:", GameManager.player_health)

func _on_fin_juego_body_entered(_body: Node2D) -> void:
	if GameManager.has_all_items():
		print("Has ganado el juego")
		get_tree().change_scene_to_file("res://Assets/Scenes/treasoure.tscn")
	else:
		print("No tienes todos los objetos necesarios para ganar")

func recogida_gasofa() -> void:
	GameManager.has_gasoline1 = true
	contador_gasofa += 1
	label_gasofa.text = str(contador_gasofa) + "/2"
	print("Has recogido gasolina 1")
	if contador_gasofa == 2:
		GameManager.has_gasoline2 = true
		label_gasofa.text = str(contador_gasofa) + "/2"
		print("Has recogido gasolina 2")

func recogida_bateria() -> void:
	GameManager.has_battery1 = true
	contador_bateria += 1
	label_bateria.text = str(contador_bateria) + "/2"
	print("Has recogido bateria 1")
	if contador_bateria == 2:
		GameManager.has_battery2 = true
		label_bateria.text = str(contador_bateria) + "/2"
		print("Has recogido bateria 2")

func recogida_llave() -> void:
	GameManager.has_key = true
	label_key.text = "1/1"
	print("Has recogido la llave")

func recogida_corazon() -> void:
	GameManager.player_health += 20
	if GameManager.player_health > 100:
		GameManager.player_health = 100
	label_vida.text = str(GameManager.player_health)
	print("Has recogido un corazón")
