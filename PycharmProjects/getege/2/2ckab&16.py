from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if (not(z and not(w)) or ((z<=w)==(x<=y)))==0:print(z,x,w,y)