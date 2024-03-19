for i in range(1,10000):
    x=i
    q=9
    l=0
    if x<q:
        t=x
        x=q
        q=t
    while x>=q:
        l+=1
        x-=q
    m=x
    if (l,m)==(4,1):print(i)