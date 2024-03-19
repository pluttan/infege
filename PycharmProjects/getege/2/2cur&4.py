from itertools import product

for x, y, z, w in product((0, 1), repeat=4):
    if (x or bool(not (y))) and not (x == z) and w:
        print(w, z, y, x)
