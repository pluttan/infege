f=lambda n:0 if n<=1 else f(n-1)+3*n**2 if n%2!=0\
    else n//2+f(n-1)+2
print(f(49))