# TASK:
# Now Draw the player rectangle
# The player rectangle should be the same dimensions as each "cell"
# in the grid
# and be able to be moved with Up, Left, Down, and Right Keys
# AND
# The grid should be able to be resizable
# When the grid is resized, the player should stay in their cell

from pyray import *

screen_size = 500

init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

num_rectangles_per_side = 5

while not window_should_close():
    begin_drawing()

    clear_background(SKYBLUE)

    if is_key_pressed(KeyboardKey.KEY_EQUAL):
        num_rectangles_per_side += 1
    if is_key_pressed(KeyboardKey.KEY_MINUS):
        num_rectangles_per_side -= 1
        if num_rectangles_per_side < 1:
            num_rectangles_per_side = 1
    

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
