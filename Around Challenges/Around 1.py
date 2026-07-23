# Reeborg's World - "Around 1" Challenge
def walk_side():
    while front_is_clear():
        move()
    turn_left()

# Repeat the side-walking process for all 4 walls
walk_side()
walk_side()
walk_side()
walk_side()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
