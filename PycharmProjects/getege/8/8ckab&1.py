from itertools import *
k=0
for a,b,c,d in product("kreslo",repeat=4):
    if a in "krsl" and d in "eo":k+=1
print(k)