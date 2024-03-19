def f(a, c, m):
    if a >= 100: return c % 2 == m % 2
    if c == m: return 0

    h = [f(a + 3, c + 1, m),
         f(a * 2, c + 1, m)]
    return all(h) if c % 2 == m % 2 else any(h)


for s in range(1, 92):
    for m in range(5):
        if f(s, 0, m):
            if m == 4: print(m, s)
            break
