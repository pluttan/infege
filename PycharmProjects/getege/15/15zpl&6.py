from itertools import *
f=lambda x,y,a: (2*y+3*x != 135) or (y>a) or (x>a)
for a in range(1,100):
    if all(f(x,y,a) for x,y in product(range(1,1000)
            ,repeat=2)):
        print(a)