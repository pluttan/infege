from itertools import *
for x,y,z in product((0,1),repeat=3):
    if (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not(y) and not(z)):
        print(z,x,y)