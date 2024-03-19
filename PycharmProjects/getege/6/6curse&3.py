for i in range(1,1000):
    s,n=0,0
    d=i
    while s<111:
        s+=8
        n+=d
    if n==28:print(i)