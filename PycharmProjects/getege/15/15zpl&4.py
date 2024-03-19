from itertools import *
f=lambda x,y,a: (2*x+y != 70) or (x<y) or (a < x)
for a in range(1,100):
    if all(f(x,y,a) for x,y in product(range(1,1000)
            ,repeat=2)):
        print(a)