for x in range(400_000_000,10_000_000_000):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    if len(dl)>=5:
        d=dl[0]*dl[1]*dl[2]*dl[3]*dl[4]
        if d%100==17 and d<=x:
            print(d,dl[4])
