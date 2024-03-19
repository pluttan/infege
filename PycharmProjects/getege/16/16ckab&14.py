from functools import lru_cache
k=0
@lru_cache(None)
def f(n):return n*n+5*n+4 if n>30 else f(n+1)+3*f(n+4) if n%2==0 else 2*f(n+2)+f(n+5)
for n in range(1,1001):k+=1 if sum(int(x) for x in str(f(n)))==27 else 0
print(k)