for i in range(174457,174506):
    dl = [d for d in range(2, int(i ** 0.5) + 1) if i % d == 0];dl += [i // d for d in dl];dl = sorted(list(set(dl)))
    if len(dl)==2:
        print(*dl)