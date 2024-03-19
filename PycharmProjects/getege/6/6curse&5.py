for i in range(1, 1000):
    s = i
    n = 80
    while s + n < 160:
        s += 15
        n -= 10
    if s <= 100: print(i)
