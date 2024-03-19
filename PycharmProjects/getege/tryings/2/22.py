for i in range(1,10000):
    x=i
    q=8
    p=10
    k1=k2=0
    while x<=100:
        k1+=1
        x+=p
    while x>=q:
        k2+=1
        x-=q
    l=x+k1
    m=x+k2
    if (l,m)==(12,19):print(i)