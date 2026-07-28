# Reeborg's World - Harvest 1 Solution
# This code is meant to be run inside the Reeborg's World Python environment.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def harvest_row():
    # Pick up the carrot at the start of the row if there is one
    if object_here():
        take()
    # Move forward 5 times to clean the rest of the 6-tile row
    for _ in range(5):
        move()
        if object_here():
            take()

# 1. Navigate from starting tile (1,1) up to the crop grid corner (3,3)
move()
move()
turn_left()
move()
move()
turn_right() # Reeborg is now at (3,3) facing East, ready to pick!

# 2. Complete all 6 rows systematically
for row in range(3):
    # Harvest the row going East
    harvest_row()
    
    # Pivot up to the next row
    turn_left()
    move()
    turn_left()
    
    # Harvest the row going West
    harvest_row()
    
    # If there are more rows left to do, pivot up to the next layer
    if row < 2:
        turn_right()
        move()
        turn_right()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
