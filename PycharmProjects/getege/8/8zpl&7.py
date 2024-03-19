from itertools import product
k=0
for i in product("aprsy",repeat=5):
    k+=1
    s="".join(i)
    if s.count("aa")==0 and s[0]=="y":print(k)