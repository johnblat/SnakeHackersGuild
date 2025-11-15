# TASK:
# Make the background start as a random color
# Every time you click the Space bar, make it a different random color

# New raylib functions needed:
# - is_key_pressed
# - get_random_value

# New raylib enum/classes to know about
# - KeyboardKey

from pyray import *

def generate_random_color() -> Color:
    ret = Color(0,0,0,255)
    ret.r = get_random_value(0, 255)
    ret.g = get_random_value(0, 255)
    ret.b = get_random_value(0, 255)
    return ret


init_window(500, 500, "Hackers Guild - Snake Workshop")

background_color = generate_random_color()

while not window_should_close():
    begin_drawing()
    clear_background(background_color)
    
    should_change_background_to_new_random_color = is_key_pressed(KeyboardKey.KEY_SPACE)
    if should_change_background_to_new_random_color:
        background_color = generate_random_color()

    end_drawing()

