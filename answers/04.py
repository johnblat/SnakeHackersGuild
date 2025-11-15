# TASK:
# Draw Five rectangles all with width = 100, height = 100
# 1. Upper Left
# 2. Upper Right
# 3. Bottom Left
# 4. Bottom Right
# 5. Screen Center



from pyray import *

screen_width = 500
screen_height = 500

init_window(screen_width, screen_height, "Hackers Guild - Snake Workshop")

while not window_should_close():
    begin_drawing()

    clear_background(BLUE)
    
    rectangle_width = 100
    rectangle_height = 100

    upper_left_rectangle = Rectangle(0, 0, rectangle_width, rectangle_height)
    draw_rectangle_rec(upper_left_rectangle, RED)
    
    upper_right_rectangle = Rectangle(
        screen_width - rectangle_width, # x
        0, # y
        rectangle_width, # width
        rectangle_height # height
    )
    draw_rectangle_rec(upper_right_rectangle, RED)
    
    bottom_left_rectangle = Rectangle(
        0, 
        screen_height - rectangle_height, 
        rectangle_width, 
        rectangle_height
    )
    draw_rectangle_rec(bottom_left_rectangle, RED)

    
    bottom_right_rectangle = Rectangle(
        screen_width - rectangle_width,
        screen_height - rectangle_height,
        rectangle_width,
        rectangle_height
    )
    draw_rectangle_rec(bottom_right_rectangle, RED)

    
    center_rectangle = Rectangle(
        screen_width/2 - rectangle_width/2,
        screen_height/2 - rectangle_height/2,
        rectangle_width,
        rectangle_height
    )
    draw_rectangle_rec(center_rectangle, RED)

    end_drawing()

