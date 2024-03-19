def f(c,e):
    return 0 if c>e\
        else 1 if c==e\
        else f(c+2,e)+f(c+4,e)+f(c+5,e)
for i in range(32,10000):
    if f(31,i)==1001:print(i)