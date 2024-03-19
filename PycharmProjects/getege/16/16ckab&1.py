f=lambda n:1 if n==0 else 3 if n==1 else 2 if n==2 else f(n-1)*f(n-3)

print(f(7))