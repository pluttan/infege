for i in range(164700,164753):
    dl = [d for d in range(1, int(i ** 0.5) + 1) if i % d == 0];dl += [i // d for d in dl];dl = sorted(list(set(dl)))
    if len(dl)==6:
        print(*dl[4:6])