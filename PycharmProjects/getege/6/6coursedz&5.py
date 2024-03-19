for i in range(1,1000):
    s=i
    s//=8
    n=2
    while s<=102:
        s+=4
        n=n*2-1
    if n == 257:print(i)