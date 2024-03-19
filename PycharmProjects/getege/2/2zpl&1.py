from itertools import product
for x,y,w,z in product((0,1), repeat=4):
    if (x or y) and not(y==z) and not(w):print(z,y,x,w)