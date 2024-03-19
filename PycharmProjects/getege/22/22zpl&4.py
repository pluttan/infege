for i in range(1,1000):
    x=i
    a,b=0,0
    while x>0:
        c=x%10
        a+=c
        if b<c:
            b=c
        x//=10
    if (a,b)==(10,6):print(i)