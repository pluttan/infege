f=lambda x,a: (x%4!=3 or x%6!=1)<=(x%36!=a)
for a in range(10000):
    if all(f(x,a) for x in range(100000)):print(a)