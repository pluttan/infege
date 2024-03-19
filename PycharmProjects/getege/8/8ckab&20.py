from itertools import *
k=0
q=[]
for a,b,c,d in product("aimrz",repeat=4):
    k+=1
    if k==211:print(a,b,c,d)