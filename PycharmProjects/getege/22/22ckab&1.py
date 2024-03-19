for i in range(1,100000000):
    x=i
    a,b=0,0
    while x>0:
        a+=1
        if x%11>b:
            b=x%11
        x//=11
    if (a,b)==(7,7):print(i)