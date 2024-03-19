for i in range(1,1000):
    s,k=5,0
    d=i
    while s<d:
        k+=2
        s+=k
    if s==161:print(i)