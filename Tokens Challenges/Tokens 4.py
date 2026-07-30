# Reeborg's World - Tokens 2
while not at_goal():

    if object_here():
        take()
    else:
        while carries_object():
            put()
    move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
