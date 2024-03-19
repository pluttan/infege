from itertools import product

for x, y, z in product((0, 1), repeat=3):
    if not ((x or y) <= (x == z)):
        print(x, z, y)
