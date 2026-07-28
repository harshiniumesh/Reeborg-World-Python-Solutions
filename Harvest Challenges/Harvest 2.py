# Reeborg's World - Harvest 2
# This code is meant to be run inside the Reeborg's World Python environment.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def harvest_row():
    # 1. Clear ALL carrots at the start of the row if present
    while object_here():
        take()
    # 2. Step forward 5 times to traverse the 6-tile row
    for _ in range(5):
        move()
        while object_here():
            take()

# --- Step 1: Navigate from (1,1) up to the garden corner (3,3) ---
move()
move()
turn_left()
move()
move()
turn_right()  # Reeborg is now at (3,3) facing East

# --- Step 2: Clear all 6 rows without leaving any carrots behind ---
for row in range(3):
    # Harvest the row walking East
    harvest_row()
    
    # Pivot up to the next row
    turn_left()
    move()
    turn_left()
    
    # Harvest the row walking West
    harvest_row()
    
    # If there are more rows left to go, pivot up to the next tier
    if row < 2:
        turn_right()
        move()
        turn_right()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
