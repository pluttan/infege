for i in range(1,1000):
    x=i
    s=5
    while x>0:
        if x%8>4:
            s+=x%8
        else:s*=x%8
        x//=8
    if s%100==0 and s!=0:print(i,s)