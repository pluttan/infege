from itertools import *
k=0
for a,b,c,d in permutations("vaqhy",r=4):
    s=a+b+c+d
    if a!="q" and "vh" not in s and "hv" not in s :k+=1
print(k)