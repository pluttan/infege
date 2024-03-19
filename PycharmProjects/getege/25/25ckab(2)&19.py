for x in range(113000000,114000000):
    dl=[]
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0 and d%2==0:dl += [d]
        if len(dl)>3:continue
    dl += [x // d for d in dl if d%2==0];dl = sorted(list(set(dl)))
    if len(dl)==3:print(x,dl[-2])