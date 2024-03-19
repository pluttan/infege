for i in range(136180,100000000000000):
    dl = [d for d in range(2, int(i ** 0.5) + 1) if i % d == 0];dl += [i // d for d in dl];dl = sorted(list(set(dl)))
    if sum(dl)%385==91:
        print(i,sum(dl))