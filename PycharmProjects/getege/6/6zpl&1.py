for i in range(1,10000):
    s=i
    n=1
    while s<51:
        s+=5
        n*=2
    if n==64:print(i)