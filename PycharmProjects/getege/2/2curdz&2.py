from itertools import product

for x, y, w, z in product((0, 1), repeat=4):
    if (w or (x <= y) and (bool(not z) <= x)) == 0:
        print(w, z, y, x)
