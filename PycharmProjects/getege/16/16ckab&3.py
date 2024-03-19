f=lambda n: n if n<=10 else n//4+f(n-10) if n<=36 else 2*f(n-5)
print(f(100))