from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if not(w) and ((y or z )<=(not(x) and y)):print(w,z,y,x)