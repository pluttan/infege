from itertools import product

for x, y, z, w in product((0, 1), repeat=4):
    if (x or y) and \
            (x <= bool(not (z))) and not (w):
        print(y, x, z, w)
