

# TASK:
# Keep a running window open and exit if user clicks the 'X' in the window 

# imports needed:
# - from pyray import *

# Functions needed from raylib:
# - init_window
# - window_should_close
# - begin_drawing
# - end_drawing

# control flow needed:
# - while
# - not

from pyray import *

init_window(500, 500, "Hackers Guild - Snake Workshop")

while not window_should_close():
    begin_drawing()
    end_drawing()

