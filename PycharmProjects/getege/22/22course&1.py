for i in range(1,100000):
    x=i
    l=0;m=0
    while x>0:
        l+=1
        if m<x:m=(x%10*2)
        x//=10
    if (l,m)==(3,10):print(i)