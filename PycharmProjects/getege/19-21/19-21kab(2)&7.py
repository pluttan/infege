def f(a, c, m):
    if a >= 22: return c % 2 == m % 2
    if c == m: return 0

    h = [f(a + 1, c + 1, m), f(a + 2, c + 1, m)]
    if a % 2 == 1: h += [f(a * 2, c + 1, m)]
    return all(h) if c % 2 == m % 2 else any(h)


for s in range(1, 22):
    for m in range(10):
        if f(s, 0, m):
            if m == 5: print(m, s)
            break
