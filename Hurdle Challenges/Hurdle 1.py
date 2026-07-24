# This code runs inside the Reeborg's World Python editor

def turn_right():
    """Turns the robot right by turning left three times."""
    turn_left()
    turn_left()
    turn_left()

def jump():
    """Makes the robot jump over a hurdle."""
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Main loop: keep going until the goal is reached
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

    



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
