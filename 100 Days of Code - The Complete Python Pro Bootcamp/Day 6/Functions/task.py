def turn_right()
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()

    while not wall_on_right():
        move()

    turn_right()
    move()
    turn_right()
    move()
    
    while front_is_clear():
        move()
    
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()