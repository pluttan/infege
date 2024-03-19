def f(c,e):
    return 0 if c>e\
        else 1 if c==e\
        else f(c+1,e)+f(c+3,e)+f(c*2,e)
print(f(3,9)*f(9,12)*f(12,20))