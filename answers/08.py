# TASK:
# Draw a series of rectangle lines in a grid, all evenly spaced.
# Make it so that when you press + or -, it adds the number of rectangles on 
# the sides of the grid

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
                row_index * rectangle_size,
                col_index * rectangle_size,
                rectangle_size,
                rectangle_size
            )
            draw_rectangle_lines_ex(rectangle, 2, RED)

    end_drawing()
