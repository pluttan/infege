for i in range(1,10000000):
    x=i
    a,b=0,0
    while x>0:
        d=x%7
        if d%2==0:a+=1
        else:b+=1
        x//=7
    if (a,b)==(3,4):print(i)

