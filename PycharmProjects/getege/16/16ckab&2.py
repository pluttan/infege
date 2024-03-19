f=lambda n: n if n<=3 else n*n*n+f(n-1) if n%3==0 else 4+f(n//3) if n%3==1 else n*n+f(n-2)

print(f(100))