from itertools import product
k=0
for i in product("elnocv",repeat=5):
    k+=1
    s="".join(i)
    print(k,s)
    if s.count("e")<=1 and s.count("l")==0:print(k)