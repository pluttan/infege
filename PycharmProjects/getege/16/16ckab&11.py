from functools import *
@lru_cache(None)
def f(n):return 1 if n==1 else f(n-1)-2*g(n-1)
@lru_cache(None)
def g(n):return 1 if n==1 else f(n-1)+g(n-1)+n
print(sum(int(i) for i in str(g(36))))