for x in range(1, 500):
    a = 3 * 7**(x + 1) + 13 * 7**(x + 2) + 31 * 7**(3 * x) + 7**(2 * x)
    k=0
    while a>0:
        k+=a%7
        a//=7
    if k==18:print(x)