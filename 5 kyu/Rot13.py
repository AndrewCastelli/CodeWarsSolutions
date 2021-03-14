def rot13(message):
    alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' * 10
    m = 'JimmyJohns'
    rot = []

    for letter in message:
        if letter in alpha:
            t = alpha.index(letter) + 13
            rot.append(alpha[t])
        else:
            rot.append(letter)

    return ''.join(rot)
