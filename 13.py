# TASK:
#
# 1. The Food should never spawn on any part of the snake's body. Make that happen.
# 2. Once the snake length is the entire grid, make snake be size of 1 (start a new games)



from pyray import *


def random_cell(grid_size) -> Vector2:
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


def snake_head_index(snake) -> int:
    ret = len(snake) - 1
    return ret

def snake_head(snake) -> Vector2:
    ret = snake[snake_head_index(snake)]
    return ret

screen_size = 500
grid_size = 8
max_grid_index = grid_size - 1
should_show_grid = False

snake = [
    Vector2(0, 0),
    Vector2(1, 0),
    Vector2(2, 0),
    Vector2(3, 0),
    Vector2(4, 0),
    Vector2(5, 0),
    Vector2(6, 0),
    Vector2(7, 0),
]
food = random_cell(grid_size)

init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

while not window_should_close():
    if is_key_pressed(KeyboardKey.KEY_EQUAL):
        grid_size += 1
    
    if is_key_pressed(KeyboardKey.KEY_MINUS):
        grid_size -= 1
        if grid_size < 1:
            grid_size = 1

    if is_key_pressed(KeyboardKey.KEY_F1):
        should_show_grid = not should_show_grid

    move_amount = Vector2(0, 0)

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
        new_snake_head = vector2_add(snake_head(snake), move_amount)
        will_snake_eat_food = vector2_equals(new_snake_head, food)
        if will_snake_eat_food:
            snake.append(new_snake_head)
            food = random_cell(grid_size)
        else:
            for i in range(0, snake_head_index(snake)):
                snake[i] = vector2_copy(snake[i+1])
            snake[snake_head_index(snake)] = new_snake_head

    begin_drawing()
    clear_background(SKYBLUE)

    snake_head_rectangle = vector2_to_grid_rectangle(snake_head(snake), screen_size, grid_size)
    draw_rectangle_rec(snake_head_rectangle, WHITE)

    for i in range(0, snake_head_index(snake)):
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

    end_drawing()