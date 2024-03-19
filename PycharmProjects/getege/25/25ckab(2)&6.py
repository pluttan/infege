for x in range(550000,10000000000):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    if len(dl)>0:
        q=sum(dl)//len(dl)
        if q%31==13:print(x,int(q))