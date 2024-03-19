for i in range(1,1000):
    x=i
    p,s=1,0
    while x>0:
        if x%2==0:
            p*=x%10
        else:s+=x%10
        x//=10
    if (s,p)==(5,24):print(i)