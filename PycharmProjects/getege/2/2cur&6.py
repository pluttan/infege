from itertools import product

for x, y, z, w in product((0, 1), repeat=4):
    if (not (y <= w) or (x == z) or x) == 0:
        print(z, y, w, x)
