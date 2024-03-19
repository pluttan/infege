for i in range(1,1000):
    a=i
    r=13
    l=0
    while a>=r:
        l+=1
        a-=r
    m=a
    if m<l:
        m=l
        l=a
    if (l,m)==(9,12):print(i)