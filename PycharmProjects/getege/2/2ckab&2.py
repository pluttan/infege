from itertools import *
for a,b,c in product((0,1),repeat=3):
     print(a,b,c,(a and not(c)) or (not(b) and not(c)))