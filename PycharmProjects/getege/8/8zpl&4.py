from itertools import product
k=0
for i in product("gepard",repeat=5):
    s="".join(i)
    if s.count("g")==1 and s[0]!="a" and s[-1]!="e":k+=1
print(k)