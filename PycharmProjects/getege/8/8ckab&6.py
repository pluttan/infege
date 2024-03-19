from itertools import *
k=0
for a,b,c,d,e in product("igrok",repeat=5):
    s= a+b+c+d+e
    for i in s:
        if s.count(i)!=1:break
    else:
        if "rok" not in s and a!="k":k+=1
print(k)