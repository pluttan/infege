def f(c,e):
    return 0 if c>e or c == 43\
        else 1 if c==e\
        else f(c+2,e)+f(2*c-1,e)+f(2*c+1,e)
print(f(7,63))