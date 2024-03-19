def f(a,c,m):
    if a<=0:return c%2==m%2
    if c==m:return 0

    h=[f(a-i,c+1,m) for i in range(1,a//2+1)]
    return any(h) if c%2!=m%2 else all(h)
for s in range(1,100):
    for m in range(1,5):
        if f(s,0,m):
            if m%2==0:print(s,m)
            break