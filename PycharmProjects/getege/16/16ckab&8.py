f=lambda n:1 if n==1 else 2 if n==2 else (n+f(n-2))//5 if n%2==0 else (2*n+f(n-1)+f(n-1))//4
print(f(50))