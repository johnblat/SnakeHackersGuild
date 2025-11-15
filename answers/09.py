# TASK:
# Now Draw the player rectangle
# The player rectangle should be the same dimensions as each "cell"
# in the grid
# and be able to be moved with Up, Left, Down, and Right Keys
# AND
# The grid should be able to be resizable
# When the grid is resized, the player should stay in their cell


from pyray import *

screen_size = 500

init_window(screen_size, screen_size, "Hackers Guild - Snake Workshop")

num_rectangles_per_side = 5

player = Rectangle(0, 0, 1, 1)

while not window_should_close():
    begin_drawing()

    clear_background(SKYBLUE)

    if is_key_pressed(KeyboardKey.KEY_EQUAL):
        num_rectangles_per_side += 1
    if is_key_pressed(KeyboardKey.KEY_MINUS):
        num_rectangles_per_side -= 1
        if num_rectangles_per_side < 1:
            num_rectangles_per_side = 1

    if is_key_pressed(KeyboardKey.KEY_UP):
        player.y -= 1
    elif is_key_pressed(KeyboardKey.KEY_DOWN):
        player.y += 1
    elif is_key_pressed(KeyboardKey.KEY_LEFT):
        player.x -= 1
    elif is_key_pressed(KeyboardKey.KEY_RIGHT):
        player.x += 1
    
    rectangle_draw_size = screen_size / num_rectangles_per_side

    player_draw_rectangle = Rectangle(
        player.x * rectangle_draw_size, 
        player.y * rectangle_draw_size, 
        player.width * rectangle_draw_size, 
        player.height * rectangle_draw_size
    )
    draw_rectangle_rec(player_draw_rectangle, WHITE)

    for row_index in range(0, num_rectangles_per_side):
        for col_index in range(0, num_rectangles_per_side):
            rectangle = Rectangle(
                col_index * rectangle_draw_size,
                row_index * rectangle_draw_size,
                rectangle_draw_size,
                rectangle_draw_size
            )
            draw_rectangle_lines_ex(rectangle, 2, RED)

    

    end_drawing()
