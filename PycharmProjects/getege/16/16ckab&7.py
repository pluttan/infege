f=lambda n:3 if n<=3 else f(n//2)+5 if n%2==0 else f(n-1)-f(n-2)
print(f(20))