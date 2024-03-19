f=lambda c,e:0 if c>e else 1 if c==e else f(c+1,e)+f(c*2,e)+f(c*c,e)
print(f(5,154))