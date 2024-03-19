from itertools import *
k=0
q=[]
for a,b,c,d in product("elmur",repeat=4):
    k+=1
    if a=="l":print(k);break