# Reeborg's World - Around 1: Apple
# This code assumes the apple is directly in front of Reeborg at the start.
# Function to move one step and pick up an apple if it exists
def move_and_pick():
    move()
    if object_here():
        take()

# Walk all 4 sides of the square map
for i in range(4):
    while front_is_clear():
        move_and_pick()
    turn_left()



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
