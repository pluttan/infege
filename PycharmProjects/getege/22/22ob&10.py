for i in range(135,136):
    n=i
    c=0
    t=3
    d=3
    while n!=0:
        n-=t
        t+=d
        c+=1
    if c%2==0:
        c+=d
    if c==9:print(i)