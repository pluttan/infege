for x in range(6080068,6080177):
    dl = [d for d in range(2, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    if dl==[]:print(x)