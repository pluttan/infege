for i in range(1,100000):
    x=i
    s=1
    a=11
    while x//7>0:
        if x%7<4:
            s+=a
        else:
            s+=x%7
        x//=7
    if s==26:print(i)