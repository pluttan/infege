from itertools import *
k=0
for s in product("abklu",repeat=4):
    k+=1
    s = "".join(s)
    if s.count(s[0])==1 and\
            s.count(s[1])==1 and\
            s.count(s[2])==1 and\
            s.count(s[3])==1:
        print(s,k)