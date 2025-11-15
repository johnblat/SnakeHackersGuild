# TASK:
#
# 1. Add a main menu that can be toggled to with ENTER
# 2. When entering the game (leaving the main menu), the snake should reset to some default state


from pyray import *


def get_random_cell(grid_size) -> Vector2:
    max_index = grid_size - 1
    ret = Vector2(
        get_random_value(0, max_index),
        get_random_value(0, max_index)
    )
    return ret


def vector2_to_grid_rectangle(v : Vector2, screen_size : float, grid_size : float) -> Rectangle:
    rectangle_draw_size = screen_size / grid_size

    ret = Rectangle(
        v.x * rectangle_draw_size,
        v.y * rectangle_draw_size,
        rectangle_draw_size,
        rectangle_draw_size
    )
    return ret


def vector2_copy(orig : Vector2) -> Vector2:
    new_vector2 = Vector2(orig.x, orig.y)
    return new_vector2


def get_snake_head_index(snake) -> int:
    ret = len(snake) - 1
    return ret


def get_snake_head(snake) -> Vector2:
    snake_head_index = get_snake_head_index(snake)
    ret = snake[snake_head_index]
    return ret


def get_random_cell_not_on_snake(snake, grid_size : float) -> Vector2:
    remaining_cells = []
    for row_index in range(0, grid_size):
        for col_index in range(0, grid_size):
            cell = Vector2(row_index, col_index)
            cell_in_snake = False
            for _, snake_cell in enumerate(snake):
                b = vector2_equals(cell, snake_cell)
                cell_in_snake = cell_in_snake or b
            if not cell_in_snake:
                remaining_cells.append(cell)

    random_index_into_remaining_cells_list = get_random_value(0, len(remaining_cells) - 1)
    food_cell = remaining_cells[random_index_into_remaining_cells_list]
    return food_cell

LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3

screen_size = 500
grid_size = 8
max_grid_index = grid_size - 1
should_show_grid = False
should_check_for_lose = True
should_move_automatically = True
wait_duration = 0.1
wait_timer = wait_duration
snake_move_direction = RIGHT 
next_snake_move_direction = snake_move_direction
main_menu_active = True

snake = [
    get_random_cell(grid_size)
]
food = get_random_cell_not_on_snake(snake, grid_size)

init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

while not window_should_close():

    begin_drawing()
    clear_background(SKYBLUE)
    if main_menu_active:
        cell_size = int(screen_size/grid_size)
        draw_text("SNAKE",0,0,cell_size,BLACK)
        draw_text("[PRESS ENTER TO PLAY]", 0,cell_size*3, int(cell_size/2), BLACK)
        if is_key_pressed(KeyboardKey.KEY_ENTER):
            main_menu_active = False
            snake = [
                get_random_cell(grid_size)
            ]
            food = get_random_cell_not_on_snake(snake, grid_size)
    else:
        if is_key_pressed(KeyboardKey.KEY_ENTER):
            main_menu_active = True

        if is_key_pressed(KeyboardKey.KEY_EQUAL):
            grid_size += 1
        
        if is_key_pressed(KeyboardKey.KEY_MINUS):
            grid_size -= 1
            if grid_size < 1:
                grid_size = 1

        if is_key_pressed(KeyboardKey.KEY_F1):
            should_show_grid = not should_show_grid
        
        if is_key_pressed(KeyboardKey.KEY_F2):
            should_check_for_lose = not should_check_for_lose

        if is_key_pressed(KeyboardKey.KEY_F3):
            should_move_automatically = not should_move_automatically

        move_amount = Vector2(0, 0)

        if should_move_automatically:
            if is_key_pressed(KeyboardKey.KEY_UP) and snake_move_direction != DOWN:
                next_snake_move_direction = UP
            elif is_key_pressed(KeyboardKey.KEY_DOWN) and snake_move_direction != UP:
                next_snake_move_direction = DOWN
            elif is_key_pressed(KeyboardKey.KEY_LEFT) and snake_move_direction != RIGHT:
                next_snake_move_direction = LEFT
            elif is_key_pressed(KeyboardKey.KEY_RIGHT) and snake_move_direction != LEFT:
                next_snake_move_direction = RIGHT

            frame_time = get_frame_time()
            wait_timer -= frame_time
            if wait_timer <= 0:
                snake_move_direction = next_snake_move_direction

                wait_timer = wait_duration
                if snake_move_direction == UP:
                    move_amount.y = -1
                elif snake_move_direction == DOWN:
                    move_amount.y = 1
                elif snake_move_direction == LEFT:
                    move_amount.x = -1
                elif snake_move_direction == RIGHT:
                    move_amount.x = 1
        else:
            if is_key_pressed(KeyboardKey.KEY_UP):
                move_amount.y = -1
            elif is_key_pressed(KeyboardKey.KEY_DOWN):
                move_amount.y = 1
            elif is_key_pressed(KeyboardKey.KEY_LEFT):
                move_amount.x = -1
            elif is_key_pressed(KeyboardKey.KEY_RIGHT):
                move_amount.x = 1

        did_snake_move = not vector2_equals(move_amount, Vector2(0,0))
        if did_snake_move:
            new_snake_head = vector2_add(get_snake_head(snake), move_amount)
            will_snake_eat_food = vector2_equals(new_snake_head, food)
            if will_snake_eat_food:
                snake.append(new_snake_head)
                max_snake_size = grid_size * grid_size
                did_just_win = len(snake) >= max_snake_size
                if did_just_win:
                    snake = [
                        Vector2(get_snake_head(snake).x, get_snake_head(snake).y)
                    ]
                food = get_random_cell_not_on_snake(snake, grid_size)            
            else:
                for i in range(0, get_snake_head_index(snake)):
                    snake[i] = vector2_copy(snake[i+1])
                snake[get_snake_head_index(snake)] = new_snake_head

        if should_check_for_lose:
            snake_head = get_snake_head(snake)
            
            did_snake_head_collide_with_tail = False
            for i in range(0, get_snake_head_index(snake)):
                tail_cell = snake[i]
                did_snake_head_collide_with_tail = did_snake_head_collide_with_tail or vector2_equals(tail_cell, snake_head)
            
            is_snake_out_of_right_bounds = snake_head.x >= grid_size
            is_snake_out_of_left_bounds = snake_head.x < 0
            is_snake_out_of_top_bounds = snake_head.y < 0
            is_snake_out_of_bottom_bounds = snake_head.y >= grid_size

            if is_snake_out_of_right_bounds:
                snake = [
                    Vector2(grid_size - 1, snake_head.y)
                ]
                snake_move_direction = LEFT
                next_snake_move_direction = snake_move_direction
            elif is_snake_out_of_left_bounds:
                snake = [
                    Vector2(0, snake_head.y)
                ]
                snake_move_direction = RIGHT
                next_snake_move_direction = snake_move_direction
            elif is_snake_out_of_top_bounds:
                snake = [
                    Vector2(snake_head.x, 0)
                ]
                snake_move_direction = DOWN
                next_snake_move_direction = snake_move_direction
            elif is_snake_out_of_bottom_bounds:
                snake = [
                    Vector2(snake_head.x, grid_size - 1)
                ]
                snake_move_direction = UP
                next_snake_move_direction = snake_move_direction
            elif did_snake_head_collide_with_tail:
                snake = [
                    Vector2(snake_head.x, snake_head.y)
                ]
        
        begin_drawing()
        clear_background(SKYBLUE)

        snake_head_rectangle = vector2_to_grid_rectangle(get_snake_head(snake), screen_size, grid_size)
        draw_rectangle_rec(snake_head_rectangle, WHITE)

        for i in range(0, get_snake_head_index(snake)):
            snake_tail_segment_rectangle = vector2_to_grid_rectangle(snake[i], screen_size, grid_size)
            draw_rectangle_rec(snake_tail_segment_rectangle, LIGHTGRAY)

        food_rectangle = vector2_to_grid_rectangle(food, screen_size, grid_size)
        draw_rectangle_rec(food_rectangle, PINK)

        if should_show_grid:
            for row_index in range(0, grid_size):
                for col_index in range(0, grid_size):
                    cell = Vector2(col_index, row_index)
                    rectangle = vector2_to_grid_rectangle(cell, screen_size, grid_size)
                    draw_rectangle_lines_ex(rectangle, 1, BLUE)

        if not should_check_for_lose:
            cell_size = int((screen_size / grid_size)/2)
            draw_text("Can't Die!", 0, 0, cell_size, BLACK)

        if not should_move_automatically:
            cell_size = int((screen_size/grid_size)/2)
            draw_text("Manual Movement", 0, cell_size, cell_size, BLACK)
    end_drawing()