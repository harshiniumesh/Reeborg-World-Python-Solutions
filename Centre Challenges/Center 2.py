# Reeborg's World - Center - 2
# This code finds the center of the world even if the size is unknown.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def go_to_wall():
    while front_is_clear():
        move()

def count_steps():
    steps = 0
    while front_is_clear():
        move()
        steps += 1
    turn_around()
    for _ in range(steps):
        move()
    turn_around()
    return steps

def go_to_center():
    steps = count_steps()
    half = steps // 2
    for _ in range(half):
        move()

# --- Main program ---
# Step 1: Horizontal center
go_to_center()

# Step 2: Vertical center
turn_left()
go_to_center()

# Step 3: Place object at center
put()   # Drop the object/beeper at the center

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
