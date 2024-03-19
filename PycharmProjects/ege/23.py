from itertools import *
from functools import *


def m(h):
    return h + 4, h + 10, 2 * h + 1


k = 0


@lru_cache(None)
def f(h):
    global k
    if h == 27: k += 1
    if h < 27:
        for i in m(h): f(i)
f(2)
print(k)