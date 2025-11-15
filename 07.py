# TASK:
# Make a Rectangle with sides of size 50 (it's a square)
# Everytime you press up, left, right, or down
# the Rectangle will move one side distance in that direction


from pyray import *

screen_size = 500
init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

rectangle_side_size = 50
rectangle = Rectangle(0,0, rectangle_side_size, rectangle_side_size)

while not window_should_close():
    begin_drawing()
    clear_background(SKYBLUE)
    draw_rectangle_rec(rectangle, RED)
    end_drawing()

