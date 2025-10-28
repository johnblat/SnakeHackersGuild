from pyray import *



window_size = 640

grid_side_cells_count = 8
grid_cell_size = window_size / grid_side_cells_count
grid_cells_total = grid_side_cells_count * grid_side_cells_count

DIRECTION_UP: int = 0
DIRECTION_DOWN: int = 1
DIRECTION_LEFT: int = 2
DIRECTION_RIGHT: int = 3

GAME_STATE_MAIN_MENU: int = 0
GAME_STATE_PLAY: int = 1
GAME_STATE_GAMEOVER: int = 2

game_over_duration = 3.0
game_over_timer = 0.0

game_state = GAME_STATE_MAIN_MENU

snake_cells = [Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)]

snake_cells[0].x = 0
snake_cells[0].y = 3

snake_cells[1].x = 1
snake_cells[1].y = 3

snake_cells[2].x = 2
snake_cells[2].y = 3

snake_direction = DIRECTION_RIGHT

food_cell = Vector2(3,3)

snake_wait_duration = 0.2
snake_wait_timer = snake_wait_duration

def reset_snake_state():
    global snake_cells
    global food_cell
    global snake_direction 

    snake_cells.clear()
    snake_cells = [Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)]

    snake_cells[0].x = 0
    snake_cells[0].y = 3

    snake_cells[1].x = 1
    snake_cells[1].y = 3

    snake_cells[2].x = 2
    snake_cells[2].y = 3

    food_cell = Vector2(3,3)
    snake_direction = DIRECTION_RIGHT


def snake_head_index():
    return len(snake_cells) - 1


set_target_fps(60)
init_window(window_size, window_size, "Snake - Hackers Guild PGH")

while not window_should_close():

    begin_drawing()

    dt = get_frame_time()

    if game_state == GAME_STATE_MAIN_MENU:
        clear_background(GRAY)
        draw_text("SNAKE", 0, 0, 60, WHITE)
        draw_text("Press Enter to Play",0, 70, 50, WHITE)
        if is_key_pressed(KEY_ENTER):
            game_state = GAME_STATE_PLAY

    elif game_state == GAME_STATE_PLAY:
        snake_wait_timer -= dt

        if is_key_down(KEY_LEFT) and snake_direction != DIRECTION_RIGHT:
            snake_direction = DIRECTION_LEFT
        if is_key_down(KEY_RIGHT) and snake_direction != DIRECTION_LEFT:
            snake_direction = DIRECTION_RIGHT
        if is_key_down(KEY_UP) and snake_direction != DIRECTION_DOWN:
            snake_direction = DIRECTION_UP
        if is_key_down(KEY_DOWN) and snake_direction != DIRECTION_UP:
            snake_direction = DIRECTION_DOWN

        is_snake_out_of_bounds = snake_cells[snake_head_index()].x >= grid_side_cells_count or snake_cells[snake_head_index()].x < 0 or snake_cells[snake_head_index()].y < 0 or snake_cells[snake_head_index()].y >= grid_side_cells_count

        is_snake_head_colliding_with_tail = False
        for i, snake_cell in enumerate(snake_cells):
            if i == snake_head_index():
                continue
            is_snake_head_colliding_with_tail = is_snake_head_colliding_with_tail or (snake_cells[snake_head_index()].x == snake_cell.x and snake_cells[snake_head_index()].y == snake_cell.y)
        
        game_over = is_snake_head_colliding_with_tail or is_snake_out_of_bounds

        if game_over:
            reset_snake_state()
            game_state = GAME_STATE_GAMEOVER
            game_over_timer = game_over_duration
            continue

        is_snake_wait_timer_complete = snake_wait_timer <= 0
        if is_snake_wait_timer_complete:
            snake_wait_timer = snake_wait_duration

            next_cell = Vector2(0,0)

            if snake_direction == DIRECTION_RIGHT:
                next_cell.x = snake_cells[snake_head_index()].x + 1
                next_cell.y = snake_cells[snake_head_index()].y
            if snake_direction == DIRECTION_LEFT:
                next_cell.x = snake_cells[snake_head_index()].x - 1
                next_cell.y = snake_cells[snake_head_index()].y
            if snake_direction == DIRECTION_UP:
                next_cell.x = snake_cells[snake_head_index()].x
                next_cell.y = snake_cells[snake_head_index()].y - 1
            if snake_direction == DIRECTION_DOWN:
                next_cell.x = snake_cells[snake_head_index()].x
                next_cell.y = snake_cells[snake_head_index()].y + 1

            will_snake_eat_food_at_next_cell = next_cell.x == food_cell.x and next_cell.y == food_cell.y

            win = will_snake_eat_food_at_next_cell and len(snake_cells) >= grid_cells_total - 1
            if win:
                reset_snake_state()
            else:
                if will_snake_eat_food_at_next_cell:
                    snake_cells.append(Vector2(food_cell.x, food_cell.y))
                    food_cell.x = get_random_value(0, grid_side_cells_count-1)
                    food_cell.y = get_random_value(0, grid_side_cells_count-1)

                    is_food_on_empty_cell = False
                    while not is_food_on_empty_cell:
                        food_on_snake = False
                        for snake_cell in snake_cells:
                            food_on_snake = food_on_snake or (snake_cell.x == food_cell.x and snake_cell.y == food_cell.y)
                        is_food_on_empty_cell = not food_on_snake
                        if food_on_snake:
                            food_cell.x += 1
                            if food_cell.x > grid_side_cells_count - 1:
                                food_cell.x = 0
                                food_cell.y += 1
                            if food_cell.y > grid_side_cells_count - 1:
                                food_cell.x = 0
                                food_cell.y = 0

                else:
                    i = 0
                    while i < snake_head_index():
                        snake_cells[i].x = snake_cells[i+1].x
                        snake_cells[i].y = snake_cells[i+1].y
                        i+=1

                    snake_cells[snake_head_index()].x = next_cell.x
                    snake_cells[snake_head_index()].y = next_cell.y

        clear_background(GRAY)

        for index, snake_cell in enumerate(snake_cells):
            rectangle = Rectangle(snake_cell.x * grid_cell_size, snake_cell.y * grid_cell_size, grid_cell_size, grid_cell_size)
            color = LIME
            if index == snake_head_index():
                color = GREEN
            draw_rectangle_rec(rectangle, color)

        food_cell_rectangle = Rectangle(food_cell.x * grid_cell_size, food_cell.y * grid_cell_size, grid_cell_size, grid_cell_size)
        draw_rectangle_rec(food_cell_rectangle, RED)
    elif game_state == GAME_STATE_GAMEOVER:
        game_over_timer -= dt
        if game_over_timer <= 0:
            game_state = GAME_STATE_MAIN_MENU
            continue
        clear_background(BLACK)
        draw_text("GAME OVER", 0, 0, 60, RED)

    end_drawing()

close_window()
