def f(a, c, m, px):
    if a >= 43: return c % 2 == m % 2
    if c == m: return 0

    if px == "+1":
        h = [f(a + 2, c + 1, m, "+2"),
             f(a * 2, c + 1, m, "*2")]
    elif px == "+2":
        h = [f(a + 1, c + 1, m, "+1"),
             f(a * 2, c + 1, m, "*2")]
    elif px == "*2":
        h = [f(a + 2, c + 1, m, "+2"),
             f(a + 1, c + 1, m, "+1")]
    else:
        h = [f(a + 1, c + 1, m, "+1"),
             f(a + 2, c + 1, m, "+2"),
             f(a * 2, c + 1, m, "*2")]
    return all(h) if c % 2 == m % 2 else any(h)


for s in range(1, 43):
    for m in range(5):
        if f(s, 0, m, ""):
            if m == 4: print(m, s)
            break
