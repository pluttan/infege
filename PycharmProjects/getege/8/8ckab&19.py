from itertools import *
k=0
q=[]
for a,b,c,d in product("aimrz",repeat=4):
    k+=1
    if a+b+c+d=="ariz":print(k)