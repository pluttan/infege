from itertools import product

for x, y, w, z in product((0, 1), repeat=4):
    if (((z <= x) and (x <= w)) or (y == (z or x))) == 0:
        print(y, x, w, z)
