#16

from itertools import product,permutations

def F(n):
    print(n,end="")
    if n >= 3:
        F(n - 1)
        F(n - 3)
print(F(5),end="")