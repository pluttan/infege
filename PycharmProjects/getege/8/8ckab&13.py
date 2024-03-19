from itertools import *
k=0
for a,b,c in product("0123456789",repeat=3):
    if a<=b<=c and a!="0":
        k+=1
print(k)