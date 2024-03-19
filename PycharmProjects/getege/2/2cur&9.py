from itertools import product

for x, y, z in product((0, 1), repeat=3):
    if (((y or z) <= x) or x == z) == 0:
        print(y, z, x)
