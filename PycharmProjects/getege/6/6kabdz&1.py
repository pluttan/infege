for i in range(14000,10000000):
    s=i
    n=10
    while s>0:
        s-=15
        n+=3
    if n ==3010:print(i,s,n)