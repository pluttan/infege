from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if ((x==bool(not(z)))<=((x or w)==y))==0:print(x,w,y,z)