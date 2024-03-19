from itertools import *
f=lambda x,y,a:(x*y>a)and(x>y)and(x<8)
for a in range(1,1000):
    if all(f(x,y,a)==0 for x,y in product(range(1,10000),repeat=2)):print(a)