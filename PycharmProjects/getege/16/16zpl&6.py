f=lambda n:1 if n==1 else 3*n+f(n-2) if n%2==1\
    else 4*f(n//2)
print(f(42))