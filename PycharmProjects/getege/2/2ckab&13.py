from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if ((w<=y) or not(y<=z))and(not(x))and(not(x==z)):
        print(w,x,z,y)