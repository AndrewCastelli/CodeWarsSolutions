def is_valid_walk(walk):
    x = 0
    y = 0

    for d in walk:
        if d is 'n':
            x += 1
        if d is 's':
            x -= 1
        if d is 'e':
            y += 1
        if d is 'w':
            y -= 1

    if (x == 0 and y == 0) and len(walk) == 10:
        return True
    else:
        return False
