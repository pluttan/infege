from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if ((x and z) or ((w<=x)==(z<=y)))==0:
        print(x,z,y,w)