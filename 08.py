# TASK:
# Draw a series of rectangle lines in a grid, all evenly spaced.
# Make it so that when you press up or down, it adds the number of rectangles on 
# the sides of the grid

from pyray import *

screen_size = 500

init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

num_rectangles_per_side = 5
rectangle_size = screen_size / num_rectangles_per_side

while not window_should_close():
    begin_drawing()
    clear_background(SKYBLUE)


    for row_index in range(0, num_rectangles_per_side):
        for col_index in range(0, num_rectangles_per_side):
            rectangle = Rectangle(
                col_index * rectangle_size,
                row_index * rectangle_size,
                rectangle_size,
                rectangle_size
            )
            draw_rectangle_lines_ex(rectangle, 5, RED)

    end_drawing()
