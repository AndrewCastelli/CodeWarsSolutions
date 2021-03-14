def sum_square_even_root_odd(nums):
    x = []
    for n in nums:
        if n % 2 == 0:
            x.append(n ** 2)
        else:
            x.append(n ** (1 / 2))

    return round(sum(x), 2)
