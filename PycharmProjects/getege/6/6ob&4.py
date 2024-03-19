for i in range(1,100000):
    n=1
    s=i
    while s>200:
        s-=15
        n+=3
    if n==46:print(i)