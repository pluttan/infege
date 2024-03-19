from itertools import product
k=0
for a,b,c,d in product("abklu",repeat=4):
    k+=1
    print(k,a,b,c,d)
