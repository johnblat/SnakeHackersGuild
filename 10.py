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

# New Raylib function to know about:
# - vector_equals


# New Raylib classes to know about:
# - Vector2

# Reminder:
# - get_random_value

from pyray import *

screen_size = 500
num_rectangles_per_side = 5
player = Vector2(0,0)

init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

while not window_should_close():
    begin_drawing()

    clear_background(SKYBLUE)

    if is_key_pressed(KeyboardKey.KEY_EQUAL):
        num_rectangles_per_side += 1
    if is_key_pressed(KeyboardKey.KEY_MINUS):
        num_rectangles_per_side -= 1
        if num_rectangles_per_side < 1:
            num_rectangles_per_side = 1
    
    if is_key_pressed(KeyboardKey.KEY_UP):
        player.y -= 1
    elif is_key_pressed(KeyboardKey.KEY_DOWN):
        player.y += 1
    elif is_key_pressed(KeyboardKey.KEY_LEFT):
        player.x -= 1
    elif is_key_pressed(KeyboardKey.KEY_RIGHT):
        player.x += 1

    rectangle_draw_size = screen_size / num_rectangles_per_side
    player_draw_rectangle = Rectangle(
        player.x * rectangle_draw_size, 
        player.y * rectangle_draw_size, 
        rectangle_draw_size, 
        rectangle_draw_size
    )

    draw_rectangle_rec(player_draw_rectangle, WHITE)

    for row_index in range(0, num_rectangles_per_side):
        for col_index in range(0, num_rectangles_per_side):
            rectangle_size = screen_size / num_rectangles_per_side
            rectangle = Rectangle(
                col_index * rectangle_size,
                row_index * rectangle_size,
                rectangle_size,
                rectangle_size
            )
            draw_rectangle_lines_ex(rectangle, 2, RED)

    end_drawing()
