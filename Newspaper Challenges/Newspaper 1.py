# Reeborg's World - Newspaper 1 Solution
# This code is meant to run inside https://reeborg.ca
# Helper: turn right using only turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# --- STEP 1: PICK UP THE STAR NEWSPAPER ---
take("star")

# Navigate up the stairs to (1,2)
turn_left()
move()

# Move to (3,2)
turn_right()
move()
move()

# Climb to (3,3)
turn_left()
move()

# Move to (5,3)
turn_right()
move()
move()

# Climb to (5,4)
turn_left()
move()

# Walk straight to the customer door at (7,4)
turn_right()
move()
move()

# --- STEP 2: HANDLE BOTH OBJECT TYPES SEPARATELY ---
# 1. Grab all the payment tokens explicitly
while object_here("token"):
    take("token")

# 2. Drop the newspaper star explicitly
put("star")

# --- STEP 3: RETURN BACK DOWN TO THE START ---
# Turn around to face West
turn_left()
turn_left()

# Retrace steps down to (5,4)
move()
move()

# Turn South and descend to (5,3)
turn_left()
move()

# Turn West and walk to (3,3)
turn_right()
move()
move()

# Turn South and descend to (3,2)
turn_left()
move()

# Turn West and walk to (1,2)
turn_right()
move()
move()

# Turn South and descend to the start at (1,1)
turn_left()
move()

# Face the original direction (East)
turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
