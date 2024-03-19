from itertools import product
k=0
for i in product("abrts",repeat=5):
    k+=1
    s="".join(i)
    if s.count("s")==0 and s.count("aa")==0:
        print(k)
    print(k,s)