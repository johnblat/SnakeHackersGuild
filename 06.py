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

while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    end_drawing()

