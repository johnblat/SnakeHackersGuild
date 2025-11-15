# TASK:
# Draw a rectangle of width = 100 and height = 100 anywhere within the screens view

# New Functions needed from raylib:
# - draw_rectangle_rec

# New classes needed from raylib:
# - Rectangle


from pyray import *

init_window(500, 500, "Hackers Guild - Snake Workshop")

while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    end_drawing()

