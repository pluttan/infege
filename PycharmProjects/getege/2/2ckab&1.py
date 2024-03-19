from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if (x or not(y)) and not(y==z) and w:print(x,w,z,y)