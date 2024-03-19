from itertools import product

for a, b, c in product((0, 1), repeat=3):
    print(c, b, a, int((a <= b) and ((a and b) <= bool(not (c)))))
