# TASK:
# Draw 5x5 evenly spaced Rectangles on a 500 x 500 pixel grid
# Rectangles can be any color other than background color

# New raylib functions needed:
# - draw_rectangle_lines_ex
# ^ will make it so that we can draw the outline of the rectangle without filling it

# New control flow needed:
# - for i in range(start, end)


from pyray import *

screen_size = 500

init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

num_rectangles_per_side = 5
rectangle_size = screen_size / num_rectangles_per_side

while not window_should_close():
    begin_drawing()
    for row_index in range(0, num_rectangles_per_side):
        for col_index in range(0, num_rectangles_per_side):
            rectangle = Rectangle(
                col_index * rectangle_size,
                row_index * rectangle_size,
                rectangle_size,
                rectangle_size
            )
            draw_rectangle_lines_ex(rectangle, 5, PINK)

    clear_background(SKYBLUE)
    end_drawing()

