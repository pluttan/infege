for i in range(1,100000):
    s=i
    s=(i-21)//10
    n=1
    while s>0:
        n*=2
        s-=n
    if n==32:print(i)