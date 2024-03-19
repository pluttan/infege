for i in range(1,100000000):
    x=i
    a,b=2,3
    while x>0:
        d=x%4
        a*=d
        if d<3:b+=d
        x//=4
    if (a,b)==(24,16):print(i)