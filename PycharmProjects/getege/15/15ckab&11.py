from itertools import *
f=lambda x,y,a:(x>39) or (y>26) or (2*x+4*y<a)

for a in range(1,1000):
    if all(f(x,y,a) for x,y in product(range(1,10000),repeat=2)):print(a)