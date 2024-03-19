for i in range(1,10000):
    s=(i-21)//10
    n=1
    while s>0:
        n*=2
        s-=n
    if n==16:print(i)