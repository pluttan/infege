for i in range(99,10000):
    x=i
    l=x-18
    m=x+36
    while l!=m:
        if l>m:l-=m
        else:m-=l
    if m==9:print(i)