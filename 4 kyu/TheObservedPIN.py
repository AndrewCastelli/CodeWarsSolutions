from itertools import product


def get_pins(observed):
    perms = ['08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968']
    return [''.join(pin) for pin in product(*(perms[int(n)] for n in observed))]
