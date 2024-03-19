for x in range(1,100000000000):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];
    dl += [x // d for d in dl];
    dl = sorted(list(set(dl)))
    if len(dl)==1000:print(x,dl)