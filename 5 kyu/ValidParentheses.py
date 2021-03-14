def valid_parentheses(string):
    count = 0

    for c in string:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            if count == -1:
                return False

    if count == 0:
        return True
    else:
        return False
