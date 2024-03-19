f=lambda n:1 if n<=1 else 3*n+f(n-1) if n%2==0\
    else 2*f(n-3)
print(f(30))