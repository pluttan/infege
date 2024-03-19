for x in range(250201,10000000000):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    if len(dl)>=2:
        if (max(dl)+min(dl))%123==17:
            print(x,max(dl)+min(dl))