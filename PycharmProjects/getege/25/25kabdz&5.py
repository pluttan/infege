for i in range(150000,10000000):
    dl = [d for d in range(2, int(i ** 0.5) + 1) if i % d == 0];dl += [i // d for d in dl];dl = sorted(list(set(dl)))
    if sum(dl)%13==10:
        print(i,sum(dl))