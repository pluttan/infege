from itertools import *
from functools import *


def dividers(n):
    r = []
    i = 2
    while (i * i <= n):
        if n % i == 0:
            r.append(i)
            k = n // i
            if k != i:
                r.append(k)
        i+=1
    return r


for i in range(5000000, 10000000 + 1):
    if i % 180 == 0:
        q = dividers(i)
        n = len(q)
        if n > 400 and n < 440:
            print(i, max(q))
