def f(c,e):
    return 0 if c<e\
        else 1 if c==e\
        else f(c-8,e)+f(c//2,e)
print(f(102,43)*f(43,5))