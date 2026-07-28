# Reeborg's World - Rain - 1 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Step into the house and onto the green goal tile
move()

# Turn to face the wall and take one step to get off the goal tile 
# so the loop can start properly
turn_right()
move()

# Keep walking the perimeter of the house until Reeborg returns to the start
while not at_goal():
    
    # If there is no wall on the right, it's an open window!
    if right_is_clear():
        turn_right()
        build_wall()
        turn_left()
        
    # If the path ahead is clear, keep walking along the wall
    if front_is_clear():
        move()
    # If there is a wall in front (a corner), turn left to follow the room
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
