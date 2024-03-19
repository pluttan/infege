for i in range(10000000,1000000000):
    x=i
    a,b=0,0
    while x>0:
        a+=1
        d=x%10
        if d%3==0:
            b+=d
        x//=10
        if a>9 or b>67:break
    if (a,b)==(8,66):print(i)