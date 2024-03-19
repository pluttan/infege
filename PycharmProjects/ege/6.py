from itertools import *
from functools import *


def f(s):
    n = 2
    while s // n > 0: s -= 5;n += 2
    return n


for i in range(1000):
    if f(i) == 20:
        print(i, f(i))
