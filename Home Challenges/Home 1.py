# Reeborg's World - Home 1 Solution
# This code runs inside Reeborg's World Python editor

def turn_right():
    """Turn right by turning left three times."""
    turn_left()
    turn_left()
    turn_left()

# Move until Reeborg reaches the goal
while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_left()



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
