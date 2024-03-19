f=lambda c,e:0 if c>e else\
    1 if c==e else\
    f(c+2,e)+f(c*2,e)
print(f(1,18)*f(18,52))
