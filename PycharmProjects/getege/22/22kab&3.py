for i in range(10000000,1000000000):
    x=i
    a,b=0,0
    while x>0:
        d=x%15
        if d%2!=0:
            a+=1
        else:b+=1
        x//=15
    if (a,b)==(4,2):
        print(i)