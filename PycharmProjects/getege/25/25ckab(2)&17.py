for x in range(106732567,152673836):
    dl=[]
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:dl += [d]
        if len(dl)>2:continue
    dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    if len(dl)==3:print(x,dl[-1])
