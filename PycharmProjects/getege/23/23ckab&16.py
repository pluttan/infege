def f(c,e):
    return 0 if c>e\
        else 1 if c==e\
        else f(c+1,e)+f(c*3//2,e) if c%2==0\
        else f(c+1,e)
print(f(1,20))