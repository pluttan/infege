for x in range(500000,1204380):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    s=[d for d in dl if d%10==8 and d!=8]
    if s!=[]:print(x,s[0])