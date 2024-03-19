for i in range(1,1000):
    s=i
    n=0
    while s+n<=300:
        s-=5
        n+=25
    if n==250:print(i)