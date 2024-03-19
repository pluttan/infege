for i in range(1,10000):
    s=i
    n=100
    while s-n>=100:
        s+=20
        n+=40
    if s!=i:print(i)

f=lambda s,c,m:c%2==m%2 if s>=30 else 0 if c==m else any([f(s+2,c+1,m),f(s+3,c+1,m),f(s*2,c+1,m)]) if (c+1)%2==m%2 else all([f(s+2,c+1,m),f(s+3,c+1,m),f(s*2,c+1,m)])