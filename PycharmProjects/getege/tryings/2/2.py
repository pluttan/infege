from itertools import *
for x,w,y,z in product((0,1),repeat=4):
    if (not(x<=w) or (y==z) or y)==0:
        print(z,x,w,y)