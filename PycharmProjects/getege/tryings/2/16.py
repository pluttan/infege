f=lambda n:2 if n<3 else\
    f(n-2)+f(n-1)-n if n%2==0 else\
    f(n-1)-f(n-2)+2*n
print(f(32))