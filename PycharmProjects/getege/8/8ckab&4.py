from itertools import *
k=0
for a,b,c,d in product("lodka",repeat=4):
    s=a+b+c+d
    if s.count("o")>=2:k+=1
print(k)