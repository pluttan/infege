from itertools import product

for a, b, c, d in product((0, 1), repeat=4):
    if ((a and b) == bool(not (c))) and (b <= d):
        print(c, b, a, d)
