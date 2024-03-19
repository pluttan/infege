from itertools import product
k=0
for i in product("elmru",repeat=4):
    k+=1
    s="".join(i)
    print(s,k)
    if s[0]=="l":print(k)
