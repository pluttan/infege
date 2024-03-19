def f(a, b, c, m):
    if a + b >= 133: return c % 2 == m % 2
    if c == m: return 0

    h = [f(a + 1, b, c + 1, m), f(a * 4, b, c + 1, m),
         f(a, b + 1, c + 1, m), f(a, b * 4, c + 1, m)]
    return all(h) if c % 2 == m % 2 else any(h)


for s in range(1, 126):
    for m in range(5):
        if f(s, 7, 0, m):
            if m == 4: print(m, s)
            break
