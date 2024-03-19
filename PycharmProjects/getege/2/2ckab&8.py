from itertools import *
for x,y,z,w in product((0,1),repeat=4):
    if not(y)and x and (not(z) or w):
        print(w,x,z,y)