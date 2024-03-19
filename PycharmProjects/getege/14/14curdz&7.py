for x in range(1, 1000):
    a = 36**17 - 6**x + 71
    k = 0
    while a > 0:
        k += a % 6
        a //= 6
    if k == 61: print(x)
