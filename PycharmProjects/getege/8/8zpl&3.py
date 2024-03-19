from itertools import product
k=0
for i in product("01234",repeat=6):
    s="".join(i)
    if s[-1] not in "34" and s[0]!=1:k+=1
print(k)