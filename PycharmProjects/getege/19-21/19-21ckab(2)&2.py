def f(a,c,m):
    if a==0: return c%2==m%2
    if a<0:return 0
    if c==m:return 0

    h=[f(a-1,c+1,m),f(a-2,c+1,m),f(a-4,c+1,m)]
    return any(h) if c%2!=m%2 else all(h)
for s in range(1,16):
    for m in range(1,100):
        if f(s,0,m):
            print(s,m)
            break