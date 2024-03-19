from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if ((y<=(x or z))and(z<=y))==0:
        print(z,w,y,x)