from math import prod


def find_difference(a, b):
    return prod(a) - prod(b) if prod(a) > prod(b) else prod(b) - prod(a)
