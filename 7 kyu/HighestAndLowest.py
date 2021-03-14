def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split()]
    new_list = max(numbers), min(numbers)

    return ' '.join(map(str, new_list))
