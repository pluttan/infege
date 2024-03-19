def f(a, c, m):
    if a > 20: return c % 2 == m % 2
    if c == m: return 0

    h = [f(a + 1, c + 1, m), f(a + 2, c + 1, m), f(a + 3, c + 1, m)]
    return any(h) if c % 2 != m % 3 else all(h)


k = 0
for s in range(1, 21):
    for m in range(1, 16):
        if f(s, 0, m):
            if m % 2 == 0: k += 1
            break
print(k)
