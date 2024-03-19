f=lambda n:1+2*n if n<5 else 2*(n+1)*f(n-2) if n%3==0 else 2*n+1+f(n-1)+2*f(n-2)
print(f(15))