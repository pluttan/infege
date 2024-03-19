from itertools import *
from functools import *


def t(x, n):
    for i in n:
        if x == i: return True
    return False


for a in range(1, 1000):
    for x in range(1, 1):
        if (t(x, (2, 4, 8, 12, 15)) <= (not (t(x, (3, 6, 8, 15))) or x == a)) == 0:
            break
    else:
        print(a)
