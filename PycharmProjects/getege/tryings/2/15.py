f = lambda x, a: ((x % 3 == 0) <= (x % 5 != 0)) \
                 or (x + a >= 90)
for a in range(1,100):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
