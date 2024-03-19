def f(a, b, c, m):
    if a + b <= 32: return c % 2 == m % 2
    if c == m: return 0

    h = [f(a - 1, b, c + 1, m), f(a // 2 + a % 2, b, c + 1, m),
         f(a, b - 1, c + 1, m), f(a, b // 2 + b % 2, c + 1, m)]
    return all(h) if c % 2 == m % 2 else any(h)


for s in range(23, 10000):
    for m in range(5):
        if f(s, 10, 0, m):
            if m == 4: print(m, s)
            break
