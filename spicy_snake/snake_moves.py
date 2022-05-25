
VALID_DIRECTIONS = {"left","right","up","down"}

def move(current_position,direction):
    assert direction in VALID_DIRECTIONS
    x,y = current_position

    if isinstance(x) != int or isinstance(y) != int:
        raise Exception("x and y have to be integers")
    

    if direction == "right":
        new_position = x+1,y
        return new_position

    elif direction == "up":
        new_position = x,y+1
        return new_position

    elif direction == "down":
        new_position = x,y-1
        return new_position

    else:
        new_position = x-1,y
        return new_position