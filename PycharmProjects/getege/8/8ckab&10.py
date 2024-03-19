from itertools import *
k=0
for a,b,c,d,e,f in product("visna",repeat=6):
    s=a+b+c+d+e+f
    if s.count("v")<=1 and a!="s" and f!="a" and f!="i":k+=1
print(k)