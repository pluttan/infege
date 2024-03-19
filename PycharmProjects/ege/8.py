from itertools import *
from functools import *
k=0
for i in product(range(6), repeat=5):
    s = "".join(map(str, i))
    if s.count("5")==3:
        k+=1
print(k)