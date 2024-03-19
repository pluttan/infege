from functools import lru_cache
@lru_cache(None)
def f(n):return n+3 if n<=18 else (n//3)*f(n//3)+n-12 if n%3==0 else f(n-1)+n*n+5
k=0
for n in range(1,1000):k+=1 if all(int(x)%2==0 for x in str(f(n))) else 0
print(k)