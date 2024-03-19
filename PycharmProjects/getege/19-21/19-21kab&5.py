from functools import lru_cache


@lru_cache(None)
def f(a, c, m):
    if a <= 0: return c % 2 == m % 2
    # if a < 0: return 0
    if c == m: return 0

    h = []
    for i in range(1, a // 2 + 2):
        if a != i: h += [f(a - i, c + 1, m)]
    
    return any(h) if c % 2 != m % 2 else all(h)


for s in range(10, 100):
    for m in range(100):
        if f(s, 0, m):
            print(m + 1, s)
            break
