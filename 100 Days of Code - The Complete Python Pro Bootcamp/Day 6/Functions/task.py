def turn_right():
    turn_left()
    turn_left()
    turn_left()

def front_is_clear():
    print("ok bud")
def move():
    print("ok bud")
def at_goal():
    print("ok bud")
def wall_in_front():
    print("ok bud")
def turn_left():
    print("ok bud")
def wall_on_right():
    print("ok bud")
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