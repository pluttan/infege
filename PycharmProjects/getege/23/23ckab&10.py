def f(c,e):
    return 0 if c>e or c==6\
        else 1 if c==e\
        else f(c+2,e)+f(c*3,e)
print(f(1,25)*f(25,63))