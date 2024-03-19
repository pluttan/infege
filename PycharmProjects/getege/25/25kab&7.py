for i in range(452_022,1000000000):
    dl = [d for d in range(2, int(i ** 0.5) + 1) if i % d == 0];dl += [i // d for d in dl];dl = sorted(list(set(dl)))
    try:
        if (dl[0]+dl[-1])%7==3:
            print(i,dl[0]+dl[-1])
    except:pass