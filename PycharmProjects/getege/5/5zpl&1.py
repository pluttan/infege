for x in range(1,10000):
    i=bin(x)[2:]
    i += str(sum(map(int, list(i))) % 2)
    i += str(sum(map(int, list(i))) % 2)
    if int(i,2)>77:print(x)