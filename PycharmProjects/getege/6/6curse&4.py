for i in range(1,100000):
    s=i
    n=200
    while s//n>=2:
        s+=5
        n+=5
    if len(str(s))==3:print(i)