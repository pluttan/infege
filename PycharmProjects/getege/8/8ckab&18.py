from itertools import *
k=0
q=[]
for a,b,c,d in product("agilmort",repeat=4):
    k+=1
    if c=="i" and d=="m":print(k)