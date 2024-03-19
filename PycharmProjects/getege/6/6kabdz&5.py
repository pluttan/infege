for i in range(1000000,1000000000):
    s=i
    s//=3
    n=0
    k=1
    while s>k:
        s-=k
        k*=2
        n+=1
    if n==20:
        print(i)
        break