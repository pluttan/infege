#22

from itertools import product,permutations

def f(x):
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L + 1
        x = x // 2
    return(L,M)
for x in range(1,1000):
    if f(x)==(5,7):print(x)