for x in range(190201,190261):
    dl = [d for d in range(1, int(x ** 0.5) + 1) if x % d == 0];dl += [x // d for d in dl];dl = sorted(list(set(dl)))
    dl=[d for d in dl if d%2==0]
    if len(dl)==4:print(*dl[2:4][::-1])