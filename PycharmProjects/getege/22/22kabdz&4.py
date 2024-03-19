for i in range(95,96):
    n=i
    c=0;t=5;d=5
    while n!=200:
        n+=t
        t+=d
        c+=1
    if c%2!=0:
        c+=d
    if c==6:print(i)