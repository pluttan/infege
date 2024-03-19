# 19

from itertools import product, permutations
from functools import lru_cache


def m(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(None)
def f(h):
    if sum(h) >= 50: return "W"
    if any(f(l) == "W" for l in m(h)): return "P1"
    if all(f(l) == "P1" for l in m(h)): return "B1"
    if any(f(l) == "B1" for l in m(h)): return "P2"
    if all(f(l) == "P2" or f(l) == "P1" for l in m(h)): return "B1/2"


for s in range(1, 42):
    h = (8, s)
    print(s, f(h))
