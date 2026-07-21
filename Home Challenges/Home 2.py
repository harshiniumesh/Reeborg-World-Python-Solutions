# Reeborg's World - Home 2 Solution
# This code runs inside https://reeborg.ca in Python mode.

# Helper function to turn right (Reeborg only has turn_left)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Function to follow the right-hand wall
def follow_right_wall():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# Main loop: keep moving until Reeborg reaches the goal
while not at_goal():
    follow_right_wall()



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
