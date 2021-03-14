def is_isogram(string):
    string = string.lower()
    for c in string:
        if string.count(c) > 1:
            return False
    return True
