from functools import*

def f(n): return 1 if n==0 else 3 if n==1 else f(n-1)-f(n-2)+3*n
print(f(40))