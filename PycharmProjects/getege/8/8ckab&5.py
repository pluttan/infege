from itertools import product
k=0
for a,b,c,d,e,f in product("salo",repeat=6):
    if 1<=(a+b+c+d+e+f).count("o")<=3:k+=1
print(k)