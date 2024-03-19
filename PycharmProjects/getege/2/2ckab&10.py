from itertools import *
for x,y,z in product((0,1),repeat=3):
    print(y,x,z,not(x==(y<=z)))