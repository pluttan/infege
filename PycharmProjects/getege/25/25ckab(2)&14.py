def pr(x):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    return x if dl == [] else 0
for x in range(25317,51238):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    s=[d for d in dl if pr(d)!=0]
    if len(s)>=6:print(x,s[-1])