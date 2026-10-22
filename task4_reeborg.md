Hurdle 3:
    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    def cross():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

    while not at_goal():
        if(not wall_in_front()):
            move()
        else:
            cross()

Hurdle 4:
    def turn_right():
        turn_left()
        turn_left()
        turn_left()
    while not at_goal():
        if(wall_in_front()):
            turn_left()
        elif(right_is_clear()):
            turn_right()
            move()
            turn_right()
            move()
        else:
            move()