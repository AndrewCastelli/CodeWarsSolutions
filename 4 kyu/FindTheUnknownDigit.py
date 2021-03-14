def solve_runes(runes):
    runes = runes.replace('--', '+')

    if '+' in runes:
        return parse_rune('+', runes)
    elif '*' in runes:
        return parse_rune('*', runes)
    elif '-' in runes[1::]:
        return parse_rune('-', runes)


def parse_rune(symbol, rune):
    for i in range(0, 10):
        if str(i) not in rune:
            string_sub = rune.replace('?', str(i))
            equal = string_sub.index('=')
            operator = string_sub.index(symbol, 1)

            left_lhs = string_sub[:operator]
            right_lhs = string_sub[operator + 1:equal]
            rhs = string_sub[equal + 1::]

            proper_0s = True if check_0s(left_lhs) and check_0s(right_lhs) and check_0s(rhs) else False
            if proper_0s:
                if symbol == '*':
                    lhs = int(left_lhs) * int(right_lhs)
                elif symbol == '+':
                    lhs = int(left_lhs) + int(right_lhs)
                elif symbol == '-':
                    lhs = int(left_lhs) - int(right_lhs)

                if lhs == int(rhs):
                    return i

    return -1


def check_0s(expression):
    single = True if len(expression) == 1 else False
    all_0s = not single and expression == '0' * len(expression)
    leading_0s = not single and expression[0] == '0'
    neg_leading_0s = expression[0] == '-' and expression[1] == '0'

    if all_0s or leading_0s or neg_leading_0s:
        return False
    else:
        return True
