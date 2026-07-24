# Function to make Reeborg jump over a hurdle
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Helper function to turn right (since only turn_left() exists)
def turn_right():
    for _ in range(3):
        turn_left()

# Main loop: keep moving until the goal is reached
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

    



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
