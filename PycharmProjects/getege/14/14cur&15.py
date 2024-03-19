m = 0
for x in range(1, 100000):
    for y in range(1, 100000):
        a = (55 + 2 * 5**x) * 5**x + 55 + 5**y
        k = 0
        while a > 0:
            k += a % 5
            a //= 5
        m = max(m, k)
print(m)