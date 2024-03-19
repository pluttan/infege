from itertools import *
from functools import *


def m(h):
    return h + 1, h + 2, h * 3


@lru_cache(None)
def f(h):
    if h >= 65: return "W"
    if any(f(i) == "W" for i in m(h)): return "P1"
    if all(f(i) == "P1" for i in m(h)): return "B1"
    if any(f(i) == "B1" for i in m(h)): return "P2"
    if all(f(i) == "P2" or f(i) == "P1" for i in m(h)): return "B12"
for s in range(1,65):
    print(s,f(s))
