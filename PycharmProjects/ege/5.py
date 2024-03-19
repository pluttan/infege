from itertools import *
from functools import *


def f(n):
    n = bin(n)[2:]
    n = str(int(n[::-1]))
    n = int(n, 2)
    return n


for i in range(1, 101):
    print(i, f(i))
