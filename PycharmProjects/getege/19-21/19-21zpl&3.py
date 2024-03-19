def f(a,b,c,m):
    if a+b>=55:return c%2==m%2
    if c==m:return 0

    h=[f(a+1,b,c+1,m), f(a*2,b,c+1,m),\
       f(a,b+1,c+1,m), f(a,b*2,c+1,m)]
    return any(h) if m%2!=c%2 else all(h)
for s in range(2,49):
    for m in range(5):
        if f(s,5,0,m):
            if m==4:print(m,s)
            break