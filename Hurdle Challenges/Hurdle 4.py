# Define a function to turn right (not available by default)
def turn_right():
   turn_left()
   turn_left()
   turn_left()
# Define the jump function to navigate over hurdles
def jump():
   # Turn left to start climbing the hurdle
   turn_left()
   # Move up while there is a wall on the right
   while wall_on_right():
       move()
   # Turn right and move forward to cross the hurdle
   turn_right()
   move()
   # Turn right again and descend until the front is clear
   turn_right()
   while front_is_clear():
       move()
   # Turn left to face forward again
   turn_left()
# Main loop to navigate until the goal is reached
while not at_goal():
   if wall_in_front(): # If there's a hurdle, jump over it
       jump()
   else: # Otherwise, move forward
       move()

    



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
