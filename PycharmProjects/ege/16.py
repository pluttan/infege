from itertools import *
from functools import *
a=""
def f(n):
    print("*",end="")
    if n >=1:
        print("*",end="")
        f(n-1)
        f(n-2)
f(28)
