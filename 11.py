# TASK:
# IT'S TIME FOR A SNAKE!
#
# 1. I provided a starting snake list
# 2. Draw the entire snake and make sure the head is a different color than the tail segments
# 3. When using the arrow keys to move, make it so that it moves like the snake is supposed to
# 4. When the snake's head touches a food, the food should get placed in a random spot like we were doing before


# NOTE: 
# 
# 1. Make the grid size default to something higher now. I made it 16.
# 2. Make it so that the begin_drawing and end_drawing functions are called only before and after the actual drawing code. 
#           Gameplay code will go above.


# Optional* New raylib functions to know about:
# - vector2_add
#
# *You can do this without the function, but its also possible to do it with the function


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


screen_size = 500
grid_size = 16
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
    Vector2(8, 0),
]
snake_head_index = len(snake) - 1 # last element
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

    did_snake_eat_food = vector2_equals(snake[snake_head_index], food)
    if did_snake_eat_food:
        food = random_cell(grid_size)

    begin_drawing()
    clear_background(SKYBLUE)

    snake_head_rectangle = vector2_to_grid_rectangle(snake[snake_head_index], screen_size, grid_size)
    draw_rectangle_rec(snake_head_rectangle, WHITE)

    food_rectangle = vector2_to_grid_rectangle(food, screen_size, grid_size)
    draw_rectangle_rec(food_rectangle, PINK)

    if should_show_grid:
        for row_index in range(0, grid_size):
            for col_index in range(0, grid_size):
                cell = Vector2(col_index, row_index)
                rectangle = vector2_to_grid_rectangle(cell, screen_size, grid_size)
                draw_rectangle_lines_ex(rectangle, 1, BLUE)

    end_drawing()
