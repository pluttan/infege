from itertools import *
k=0
for a,b,c,d,e,f,g,h in product("ab123",repeat=8):
    s=a+b+c+d+e+f+g+h
    if (s.count("a")==2 and s.count("b")==0) or \
            (s.count("a") == 1 and s.count("b") == 1) or \
            (s.count("a") == 0 and s.count("b") == 2):k+=1
print(k)