def f(a, c, middle):
    if a >= 21:
        return c % 2 == middle % 2
    if c == middle:
        return 1

    h = [f(a + 1, c + 1, middle),
         f(a + 2, c + 1, middle),
         f(a + 3, c + 1, middle)]
    return any(h) if c % 2 != middle % 2 else all(h)


for s in range(1, 21):
    for m in range(2, 30):
        if f(s, 0, m):
            if m % 2 == 0:
                print(m, s)
            break
