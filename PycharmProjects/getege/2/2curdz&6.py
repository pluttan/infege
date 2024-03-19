from itertools import product

for a, b, c, d in product((0, 1), repeat=4):
    if ((a <= b) and (c <= d) or not c) == 0:
        print(b, d, c, a)
