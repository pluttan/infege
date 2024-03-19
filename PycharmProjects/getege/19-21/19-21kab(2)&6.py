def f(a, c, m, pr, ppr):
    if a >= 21: return c % 2 == m % 2
    if c == m: return 0

    h = []
    if pr != "+1": h += [f(a + 1, c + 1, m, ppr, "+1")]
    if pr != "+2": h += [f(a + 2, c + 1, m, ppr, "+2")]
    if pr != "*2": h += [f(a * 2, c + 1, m, ppr, "*2")]
    return all(h) if c % 2 == m % 2 else any(h)


for s in range(1, 21):
    for m in range(6):
        if f(s, 0, m, "", ""):
            if m == 5: print(m, s)
            break
