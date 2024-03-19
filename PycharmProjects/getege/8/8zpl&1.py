from itertools import product
k=0
for a,b,c in product("skola",repeat=3):
    s="".join([a,b,c])
    if s.count("k")==1:k+=1
print(k)