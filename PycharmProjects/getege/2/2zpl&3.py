from itertools import *
for x,y,w,z in product((0,1),repeat=4):
    if ((y<=x)or not((x<=z)and (z<=x))and not(w))==0:
        print(z,x,w,y)