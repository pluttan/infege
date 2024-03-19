def f(a,c,m):
    if 5<=a<=25:return c%2==m%2
    if c==m or c>26:return 0

    h=[f(a+i,c+1,m) for i in range(1,5)]
    return any(h) if c%2!=m%2 else all(h)
s=0
for m in range(1,10):
    if f(s,0,m):
        print(s,m)
        break