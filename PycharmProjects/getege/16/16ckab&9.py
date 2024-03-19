f= lambda n: 0 if n<=1 else f(n-1)+3*n*n if n%2==1 else n//2+f(n-1)+2
print(f(49))