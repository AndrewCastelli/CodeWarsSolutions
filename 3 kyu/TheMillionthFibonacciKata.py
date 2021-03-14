def fib(n):
    if n >= 0:
        return fibonacci(1, 0, 0, 1, n)

    if n < 0:
        a, b = 0, 1
        for x in range(0, n, -1):
            a, b = b - a, a
        return a


def fibonacci(a, b, c, d, count):
    if count == 0:
        return b

    if count % 2 == 0:
        return fibonacci(a, b, c * c + d * d, d * d + 2 * c * d, count / 2)
    else:
        return fibonacci(b * d + a * d + a * c, b * c + a * d, c, d, count - 1)
