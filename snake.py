from pyray import *

window_size = 640

grid_side_cells_count = 16
grid_cell_size = window_size / grid_side_cells_count
grid_cells_total = grid_side_cells_count * grid_side_cells_count

DIRECTION_UP: int = 0
DIRECTION_DOWN: int = 1
DIRECTION_LEFT: int = 2
DIRECTION_RIGHT: int = 3

snake_cells = [Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)]
snake_head_index = 2

snake_cells[0].x = 0
snake_cells[0].y = 3

snake_cells[1].x = 1
snake_cells[1].y = 3

snake_cells[2].x = 2
snake_cells[2].y = 3

snake_direction = DIRECTION_RIGHT

snake_wait_duration = 0.5
snake_wait_timer = snake_wait_duration

set_target_fps(60)
init_window(window_size, window_size, "Snake - Hackers Guild PGH")

while not window_should_close():

    dt = get_frame_time()

    snake_wait_timer -= dt

    if is_key_down(KEY_LEFT):
        snake_direction = DIRECTION_LEFT
    if is_key_down(KEY_RIGHT):
        snake_direction = DIRECTION_RIGHT
    if is_key_down(KEY_UP):
        snake_direction = DIRECTION_UP
    if is_key_down(KEY_DOWN):
        snake_direction = DIRECTION_DOWN

    is_snake_wait_timer_complete = snake_wait_timer <= 0
    if is_snake_wait_timer_complete:
        snake_wait_timer = snake_wait_duration
        i = 0
        while i < snake_head_index:
            snake_cells[i].x = snake_cells[i+1].x
            snake_cells[i].y = snake_cells[i+1].y
            i+=1
        if snake_direction == DIRECTION_RIGHT:
            snake_cells[snake_head_index].x += 1
        if snake_direction == DIRECTION_LEFT:
            snake_cells[snake_head_index].x -= 1
        if snake_direction == DIRECTION_UP:
            snake_cells[snake_head_index].y -= 1
        if snake_direction == DIRECTION_DOWN:
            snake_cells[snake_head_index].y += 1

    begin_drawing()
    clear_background(GRAY)

    for index, snake_cell in enumerate(snake_cells):
        rectangle = Rectangle(snake_cell.x * grid_cell_size, snake_cell.y * grid_cell_size, grid_cell_size, grid_cell_size)
        color = LIME
        if index == snake_head_index:
            color = GREEN
        draw_rectangle_rec(rectangle, color)

    end_drawing()

close_window()
