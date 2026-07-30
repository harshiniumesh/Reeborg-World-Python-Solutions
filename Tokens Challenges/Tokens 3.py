# Reeborg's World - Tokens 2
while not at_goal():
    move()
    if object_here():
        take()
    elif carries_object():
        put()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
