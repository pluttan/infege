for i in range(1,100000000000):
    x=i
    l,m,r=0,0,0
    while x>0:
        r=r*10+x%10
        x//=10
        if x<=r:m+=1
        else:l+=x%10
    if (l,m)==(14,3) and str(i).count("0")==0:print(i)