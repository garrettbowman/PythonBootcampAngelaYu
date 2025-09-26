def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right():
        if not wall_in_front():
            move()
        elif wall_in_front():
            turn_left()
            move()
        else:
            move()
    else:
        turn_right()
        move()
