m = 100000
for x in range(1, 100):
    for y in range(1, 100):
        a = 2 * 7**x + 3 * 7**(x + 1) \
            + 4 * 7**(x + 2) \
            + 5 * 7**y+6*7**(2*y)
        k = 0
        while a > 0:
            k += a % 7
            a //= 7
        if k == 8: m += 1
print(m)