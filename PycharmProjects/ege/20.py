from itertools import *
from functools import *


def f(x):
    a, b = 0, 0
    while x > 0:
        a += 1
        if x % 2 != 0:
            b += 1
        x //= 2
    return a, b


k = 0
for i in range(1, 100000000):
    if f(i) == (16, 14): k += 1
print(k)
