from functools import reduce


def parts_sums(ls):
    sums = []

    if ls:
        sum_of_parts = reduce(lambda x, y: x + y, ls)
        sums.append(sum_of_parts)

        for n in range(1, len(ls) + 1):
            sum_of_parts -= ls[n - 1]
            sums.append(sum_of_parts)

    else:
        return [0]

    return sums
