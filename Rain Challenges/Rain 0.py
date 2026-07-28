# Reeborg's World - Rain 
# Helper to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Step into the house and onto the green goal tile
move()

# Turn to face the wall and take one step to start the perimeter sweep
turn_right()
move()

# Keep hugging the wall until Reeborg returns to the green goal tile
while not at_goal():
    if front_is_clear():
        move()
        
    if wall_in_front():
        turn_left()
        
    # If there is no wall on the right, it's the open window!
    if right_is_clear():
        turn_right()
        build_wall()
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
