f=lambda n:1 if n==1 else f(n-1)-n*g(n-1)
g=lambda n:1 if n==1 else  f(n-1)+2*g(n-1)
print(g(18))