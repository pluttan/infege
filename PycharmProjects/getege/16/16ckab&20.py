from functools import lru_cache
@lru_cache(None)
def f(n):
    return n+1 if n<3 else f(n-2)+n-2 if n%2==0 else f(n+2)+n+2
k=0
for n in range(1,1000000):
    try:
        if len(str(f(n)))==5:k+=1;print(k)
    except:pass