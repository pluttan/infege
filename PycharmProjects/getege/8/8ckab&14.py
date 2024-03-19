from itertools import *
k=0
for a,b,c,d,e,f in product("deqkstra",repeat=6):
    s=a+b+c+d+e+f
    if s.count("q")==1 and s.count("d")<=1 and s.count("e")<=1 and s.count("k")<=1 and s.count("s")<=1 and s.count("t")<=1 and s.count("r")<=1and s.count("a")<=1:
        try:
            if s[s.index("q")+1] in "dqkstr":k+=1
        except:pass
print(k)