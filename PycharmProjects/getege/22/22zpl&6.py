for i in range(1,1000):
    a=i
    r=9
    l=0
    while a>=r:
        l+=1
        a-=r
    m=a
    if m<l:
        m=l
        l=a
    if(l,m)==(2,8):print(i)