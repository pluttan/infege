def f(c,e,s):
    return 0 if c>e or (c==e and s!=7)\
        else 1 if c==e and s==7\
        else f(c+1,e,s+1)+f(c+4,e,s+1)+f(c*2,e,s+1)
print(f(3,27,0))
