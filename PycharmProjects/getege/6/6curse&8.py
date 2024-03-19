for i in range(1,1000):
    s=i
    k=0
    s*=10
    while s>0:
        k+=1
        if k%3==0:s-=10
    if k>100:print(i)