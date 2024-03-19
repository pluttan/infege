for i in range(1,10000):
    s=i
    n=0
    while s**2<101:
        s+=1
        n+=2
    if n==16:print(i)