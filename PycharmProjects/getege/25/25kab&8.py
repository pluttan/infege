for i in range(500_000,1000000000):
    dl = [d for d in range(2, int(i ** 0.5) + 1) if i % d == 0];dl += [i // d for d in dl];dl = sorted(list(set(dl)))
    for i1 in dl:
        if str(i1)[-1]=="8" and i1!=8 and i1!=i:
            print(i,i1)
            break