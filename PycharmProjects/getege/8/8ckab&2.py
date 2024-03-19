from itertools import *
k=0
for a,b,c,d,e,f in product("abcwxyz",repeat=6):
    if a in "wxyz" and f in "wxyz" and b not in "wxyz" and c not in "wxyz" and d not in "wxyz" and e not in "wxyz":
        k+=1
print(k)