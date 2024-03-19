from itertools import *
k=0
for a,b,c,d,e,f in product("pula",repeat=6):
    s=(a+b+c+d+e+f)
    if s.count("u")==2:k+=1
print(k)