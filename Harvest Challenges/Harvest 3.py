# Reeborg's World - Harvest 3
# This code is meant to be run inside the Reeborg's World Python environment.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def harvest_and_plant_tile():
    # 1. Clear any carrots if they exist on this tile
    while object_here():
        take()
    # 2. Place exactly one token down (required by the blue '1')
    put()

def harvest_row():
    harvest_and_plant_tile()
    for _ in range(5):
        move()
        harvest_and_plant_tile()

# --- Step 1: Navigate from (1,1) up to the garden corner (3,3) ---
move()
move()
turn_left()
move()
move()
turn_right()  # Reeborg is now at (3,3) facing East

# --- Step 2: Snake through all 6 rows ---
for row in range(3):
    # Process the row walking East
    harvest_row()
    
    # Pivot up to the next row
    turn_left()
    move()
    turn_left()
    
    # Process the row walking West
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
