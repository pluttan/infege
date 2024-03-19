from functools import lru_cache
k=0
@lru_cache(None)
def f(n):return 1 if n==1 else f(n//2)+1 if n%2==0 else f(n-1)+n
for i in range(1,1000):
    if f(i)==19:print(i)