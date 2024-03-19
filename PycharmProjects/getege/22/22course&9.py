for i in range(1,1000):
    x=i
    q=9
    l=0
    while x>=q:
        l+=1
        x-=q
    m=x
    if m<l:
        m=l
        l=x
    if (l,m)==(4,5):print(i)