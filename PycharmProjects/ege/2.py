from itertools import *
from functools import *


for x,y,z,w in product(range(2),repeat=4):
    if (((not(x))and y)==z)and w:print(y,z,w,x)