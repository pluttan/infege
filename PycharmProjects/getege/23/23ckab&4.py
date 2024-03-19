f=lambda c,e:0 if c<e else 1 if c==e else f(c-2,e)+f(c-5,e)
print(f(23,2))