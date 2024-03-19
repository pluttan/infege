from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if ((x<=y) or not(w<=z))==0:print(z,y,w,x)