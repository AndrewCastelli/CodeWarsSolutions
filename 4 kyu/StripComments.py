def solution(string, markers):
    lines = string.split('\n')

    for words in markers:
        lines = [x.split(words)[0].rstrip() for x in lines]

    return '\n'.join(lines)
