f=lambda n:1 if n==1 else n+f(n-1) if n%2==0\
    else 2*f(n-2)
print(f(26))