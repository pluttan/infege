from itertools import *
k=0
for a,b,c,d,e in product("gepard",repeat=5):
    s=a+b+c+d+e
    if s.count("g")==1 and a!="a" and e!="e":k+=1
print(k)
