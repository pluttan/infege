f=lambda c,e:0 if c<e else 1 if c==e else f(c-1,e)+f(c-3,e)+f(c//3,e)
print(f(22,2))