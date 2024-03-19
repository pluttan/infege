from itertools import *
from functools import *

for a,b,c in product(range(2),repeat=3):
    if ((a and (not(c)))or ((not(b)) and (not(c))))!=True:
        print(a,b,c,(a and (not(c)))or ((not(b)) and (not(c))))