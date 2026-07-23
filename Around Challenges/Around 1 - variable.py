# Reeborg's World - "Around 1-variable " Challenge
# Goal: Make Reeborg go around the world once and stop at the starting point.
# Works for worlds of different sizes.

# 1. Drop a token to mark the starting line
put()

# 2. Take the first step so we aren't standing on the token anymore
move()

# 3. Walk around the perimeter until we find our token again
while not object_here():
    if front_is_clear():
        move()
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
