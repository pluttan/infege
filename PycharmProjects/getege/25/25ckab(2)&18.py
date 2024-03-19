for x in range(55000000,60000000):
    dl=[]
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0 and d%2==1:dl += [d]
        if len(dl)>5:continue
    dl += [x // d for d in dl if d%2==1];dl = sorted(list(set(dl)))
    if len(dl)==5:print(x,dl[-1])