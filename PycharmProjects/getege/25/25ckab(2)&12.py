for x in range(550000,1204380):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    s=[d for d in dl if d%10==7]
    if len(s)==3:
        print(x,s[-1])