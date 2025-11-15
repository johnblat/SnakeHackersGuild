# TASK:
# Make the background start as a random color
# Every time you click the Space bar, make it a different random color


# New raylib functions needed:
# - is_key_pressed
# - get_random_value

# New raylib enum/classes to know about
# - KeyboardKey

from pyray import *

init_window(500, 500, "Hackers Guild - Snake Workshop")

while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    end_drawing()

