def f(c,e):
    return 0 if c>e\
        else 1 if c==e\
        else f(c+1,e)+f(c*2,e)+f(c*2+1,e)+f(c*10,e)
print(f(1,15))