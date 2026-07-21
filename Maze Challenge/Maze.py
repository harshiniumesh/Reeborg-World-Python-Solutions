# Reeborg's World - Escape the Maze
# This uses the right-hand rule: always keep your right hand on the wall.

# Helper function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Main maze escape logic
def escape_maze():
    # Step 1: Face a wall on the right before starting
    while front_is_clear():
        move()
    turn_left()

    # Step 2: Follow the right-hand rule until goal is reached
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

# Run the escape
escape_maze()
    



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
