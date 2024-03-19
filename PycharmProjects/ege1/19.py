from itertools import product
from itertools import permutations
from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(None)
def f(h):
    a,b=h
    if sum(h) >= 40: return "W"
    if any(f(m) == "W" for m in moves(h)): return "P1"
    if all(f(m) == "P1" for m in moves(h)): return "B1"
    if any(f(m) == "B1" for m in moves(h)): return "P2"
    if all(f(m) == "P2" or f(m) == "P1" for m in moves(h)): return "B1/2"


for i in range(1, 31):
    h = (9,i)
    print(i,f(h))