from itertools import *

for a, b, c, d in product((0, 1), repeat=4):
    if ((a and b) == bool(not (bool(c)))) and (b <= d):
        print(c, a, d, b)
