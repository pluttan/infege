def f(n):
    return n if n<=1 else n+f(n//3) if n%3==0 else n+f(n+3)
for n in range(1,1000):
    try:
        if f(n)>100:
            print(n)
    except:pass