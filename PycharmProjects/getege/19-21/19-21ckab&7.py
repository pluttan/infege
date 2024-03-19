def f(x,y,z,c,m):
    if x+y+z>=73:return c%2==m%2
    if c==m:return 0

    h=[f(x+3,y,z,c+1,m),\
       f(x+13,y,z,c+1,m),\
       f(x+23,y,z,c+1,m),\
       f(x,y+3,z,c+1,m),\
       f(x,y+13,z,c+1,m),\
       f(x,y+23,z,c+1,m),\
       f(x,y,z+3,c+1,m),\
       f(x,y,z+13,c+1,m),\
       f(x,y,z+23,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for s in range(1,24):
    for m in range(1,5):
        if f(2,s,2*s,0,m):
            if m==4:print(s,m)
            break