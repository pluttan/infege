for i in range(1,10000):
    x=i
    l=0
    m=1
    while x>0:
        l+=x%10*m
        x//=10
        m*=10
    if sum(map(int,list(str(l))))==15:print(i)