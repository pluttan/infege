from itertools import product
k=0
for i in product("0123456",repeat=7):
    s="".join(i)
    if s.count("22")>0 and s.count("44")\
            and s[0] !="3" and s[0]!="5":k+=1
print(k)