# TASK:
# Draw Five rectangles all with width = 100, height = 100
# 1. Upper Left
# 2. Upper Right
# 3. Bottom Left
# 4. Bottom Right
# 5. Screen Center



from pyray import *

init_window(500, 500, "Hackers Guild - Snake Workshop")

while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    draw_rectangle_rec(Rectangle(25,25,100,100), RED)
    end_drawing()

