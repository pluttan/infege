from functools import lru_cache
k=0
@lru_cache(None)
def f(n):return 0 if n==0 else f(n//2) if n%2==0 else 1+f(n-1)
for n in range(1,501):k+=1 if f(n)==8 else 0
print(k)