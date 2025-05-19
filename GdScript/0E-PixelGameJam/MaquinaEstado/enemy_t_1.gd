extends CharacterBody2D

enum EnemyState { PATRULLANDO, ATACANDO, ESCAPANDO, SANANDO, MUERTO }

@export var patrol_points: Array[Node2D]
@export var target: CharacterBody2D
@export var healing_zone: Marker2D
@export var potion_nodes: Array[Node2D]
@export var attack_radius: float = 20.0
@export var attack_range: float = 100.0
@export var speed: float = 25.0

@onready var navigation_agent: NavigationAgent2D = $NavigationAgent2D
@onready var sprite: AnimatedSprite2D = $AnimatedSprite2D
@onready var chase_sound: AudioStreamPlayer2D = $ChaseSound


var current_state: EnemyState = EnemyState.PATRULLANDO
var patrol_point_index: int = 0
var health: int = 100
var regenerating := false
var current_potion: Node2D = null
var attack_cooldown := 1.5
var time_since_last_attack := 0.0

func _ready() -> void:
	call_deferred("_actor_setup")
	_start_regeneration()

func _physics_process(delta: float) -> void:
	if current_state == EnemyState.MUERTO:
		return

	match current_state:
		EnemyState.PATRULLANDO:
			_patrol()
		EnemyState.ATACANDO:
			_attack(delta)
		EnemyState.ESCAPANDO:
			_escape()
		EnemyState.SANANDO:
			_heal()

	if not navigation_agent.is_navigation_finished():
		var next_pos: Vector2 = navigation_agent.get_next_path_position()
		var direction: Vector2 = global_position.direction_to(next_pos)
		velocity = direction * speed
		move_and_slide()

		if next_pos.x < global_position.x:
			sprite.play("izquierda")
		else:
			sprite.play("default")

	time_since_last_attack += delta

func _actor_setup() -> void:
	await get_tree().physics_frame

func _set_movement_target(movement_target: Vector2) -> void:
	navigation_agent.target_position = movement_target

func _patrol() -> void:
	if navigation_agent.is_navigation_finished():
		_go_to_next_patrol_point()
	if _can_see_target() and health >= 50:
		if current_state != EnemyState.ATACANDO:
			chase_sound.play()
		current_state = EnemyState.ATACANDO
	elif health < 30:
		current_state = EnemyState.SANANDO


func _attack(_delta: float) -> void:
	if not is_instance_valid(target):
		current_state = EnemyState.PATRULLANDO
		return

	_set_movement_target(target.global_position)
	if global_position.distance_to(target.global_position) < attack_radius:
		if time_since_last_attack >= attack_cooldown:
			_attack_action()
			time_since_last_attack = 0.0

	if health < 30 and current_state != EnemyState.ESCAPANDO:
		current_state = EnemyState.ESCAPANDO
	elif global_position.distance_to(target.global_position) > attack_range:
		current_state = EnemyState.PATRULLANDO

func _escape() -> void:
	if healing_zone:
		_set_movement_target(healing_zone.global_position)
	if health < 30 and current_state != EnemyState.SANANDO:
		current_state = EnemyState.SANANDO
	elif health >= 50:
		current_state = EnemyState.PATRULLANDO

func _heal() -> void:
	if current_state == EnemyState.MUERTO:
		return

	if current_potion == null:
		current_potion = _find_available_potion()

	if current_potion and is_instance_valid(current_potion):
		var distance: float = global_position.distance_to(current_potion.global_position)
		_set_movement_target(current_potion.global_position)

		if distance < 10.0:
			if health < 100:
				health = min(health + 50, 100)

			if health >= 50:
				current_potion = null
				current_state = EnemyState.PATRULLANDO
	else:
		if healing_zone:
			_set_movement_target(healing_zone.global_position)

		if health >= 50:
			current_state = EnemyState.PATRULLANDO

func _go_to_next_patrol_point() -> void:
	if patrol_points.is_empty():
		return
	var point: Node2D = patrol_points[patrol_point_index]
	if point:
		_set_movement_target(point.global_position)
	patrol_point_index = (patrol_point_index + 1) % patrol_points.size()

func _can_see_target() -> bool:
	return is_instance_valid(target) and global_position.distance_to(target.global_position) < attack_range

func _attack_action() -> void:
	if is_instance_valid(target) and target.has_method("take_damage"):
		target.take_damage(10)

func take_damage(amount: int) -> void:
	if current_state == EnemyState.MUERTO:
		return

	health -= amount
	health = clamp(health, 0, 100)

	if health <= 0:
		current_state = EnemyState.MUERTO
		print("El enemigo ha muerto")
		queue_free()

func _start_regeneration() -> void:
	if regenerating:
		return
	regenerating = true
	while health < 100 and current_state != EnemyState.MUERTO:
		await get_tree().create_timer(5.0).timeout
		if health > 0:
			health = min(health + 10, 100)
	regenerating = false

func _find_available_potion() -> Node2D:
	for potion in potion_nodes:
		if is_instance_valid(potion):
			return potion
	return null

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group("Player"):
		_attack_action()
		body.take_damage(10)
