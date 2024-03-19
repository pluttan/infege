from itertools import product
for x,y,w,z in product((0,1), repeat=4):
    if( not(x<=z) or (w or not(z)) or w)==0:
        print(x,y,w,z)