def f(a,c,m):
    if a>=40:return c%2==m%2
    if c==m:return 0

    h=[f(a+1,c+1,m),f(a+4,c+1,m),f(a*2,c+1,m)]
    return any(h) if m%2!=c%2 else all(h)
for s in range(1,40):
    for m in range(5):
        if f(s,0,m):
            if m==4:print(m,s)
            break