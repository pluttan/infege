for i in range(1,10000):
    s=i
    s//=10
    n=1
    while s<221:
        if n%2==0:s+=13
        n+=5
    if n==11:print(i)