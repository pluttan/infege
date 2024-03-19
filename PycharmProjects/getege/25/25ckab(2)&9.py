for x in range(1204300,1204380):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    s=sum([d for d in dl if d%2==0])
    if s!=0 and s%10==0:
        print(x,s)
