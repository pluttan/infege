for i in range(499986,100000000):
    a=i
    r=17
    l=0
    while a>=r:
        l+=1
        a-=r
    m=a
    if m<l:
        m=l
        l=a
    if (l,m)==(13,29411):print(i)