# TASK:
# 1. Now There should be a food rectangle placed somewhere random that is a different color than the player
# Every time the player "eats" the food, the food should spawn at a new random location inside the map
# preserve all the features from the previous TASK.
# 
# 2. You can optionally stop showing the grid (the rectangle lines) if you want
#

# NOTE
# Since we are using grid coordinates, and every "entity" (the player, the food) will be only one cell width wide,
# We can make them "points" or "Vector2"s instead of rectangles.
# Why? Their width/height will always be equal to one cell size

# New Raylib classes to know about:
# - Vector2

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
grid_size = 5
max_grid_index = grid_size - 1
should_show_grid = False

player = Vector2(0, 0)
food = random_cell(grid_size)

init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

while not window_should_close():
    begin_drawing()

    clear_background(SKYBLUE)

    if is_key_pressed(KeyboardKey.KEY_EQUAL):
        grid_size += 1
    if is_key_pressed(KeyboardKey.KEY_MINUS):
        grid_size -= 1
        if grid_size < 1:
            grid_size = 1

    if is_key_pressed(KeyboardKey.KEY_UP):
        player.y -= 1
    elif is_key_pressed(KeyboardKey.KEY_DOWN):
        player.y += 1
    elif is_key_pressed(KeyboardKey.KEY_LEFT):
        player.x -= 1
    elif is_key_pressed(KeyboardKey.KEY_RIGHT):
        player.x += 1

    if is_key_pressed(KeyboardKey.KEY_F1):
        should_show_grid = not should_show_grid

    did_player_eat_food = vector2_equals(player, food)
    if did_player_eat_food:
        food = random_cell(grid_size)

    player_draw_rectangle = vector2_to_grid_rectangle(player, screen_size, grid_size)
    draw_rectangle_rec(player_draw_rectangle, WHITE)

    food_draw_rectangle = vector2_to_grid_rectangle(food, screen_size, grid_size)
    draw_rectangle_rec(food_draw_rectangle, PINK)

    if should_show_grid:
        for row_index in range(0, grid_size):
            for col_index in range(0, grid_size):
                rectangle = vector2_to_grid_rectangle(food, screen_size, grid_size)
                draw_rectangle_lines_ex(rectangle, 2, RED)

    

    end_drawing()
