from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if ((not(x) and y)==z)and w:print(y,z,w,x)