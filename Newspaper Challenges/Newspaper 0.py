# Reeborg's World - Newspaper Problem Solution
# This code is meant to run inside https://reeborg.ca
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# --- STEP 1: DELIVER THE NEWSPAPER ---
take()

# Turn North and move up to (1,2)
turn_left()
move()

# Turn East and walk to (3,2)
turn_right()
move()
move()

# Turn North and climb to (3,3)
turn_left()
move()

# Turn East and walk to (5,3)
turn_right()
move()
move()

# Turn North and climb to (5,4)
turn_left()
move()

# Turn East and walk to the star at (7,4)
turn_right()
move()
move()

# Drop the newspaper
put()

# --- STEP 2: RETRACE STEPS BACK TO START (1,1) ---
# Turn around to face West
turn_left()
turn_left()

# Walk back to (5,4)
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
