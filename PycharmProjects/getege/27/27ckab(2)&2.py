f=open("27Bckab(2)&2.txt")
mas=[int(q) for q in f][1:]
p=[0]*65
m=0
for x in mas:
    for y in range(65):
        if (x*y)%65==0:m+=p[y]
    p[x%65]+=1
print(m)

#test
from itertools import *
k=0
for a,b in combinations(mas,2):
    if (a*b)%65==0:k+=1
print(k)