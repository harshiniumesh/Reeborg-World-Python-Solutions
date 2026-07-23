# Reeborg's World - Around 3
# Helper function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

put()

if not front_is_clear():
    turn_left()

move()

while not object_here():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
