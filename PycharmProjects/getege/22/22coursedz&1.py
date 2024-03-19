for i in range(1,1000):
    x=i
    a=0
    b=1
    while x>0:
        if x%2>0:
            a+=1
        else:b+=x%5
        x//=5
    if (a,b)==(2,9):
        print(i)