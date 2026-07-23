# Reeborg's World - Around 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# 1. Leave a marker at the starting position
put()

# 2. Take the first step to get moving
move()

# 3. Follow the right wall until returning to the marker
while not object_here():
    if right_is_clear():
        # Corner turned inward: turn right and step into it
        turn_right()
        move()
    elif front_is_clear():
        # Straight path: keep moving forward
        move()
    else:
        # Dead end/Corner turned outward: turn left
        turn_left()



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
