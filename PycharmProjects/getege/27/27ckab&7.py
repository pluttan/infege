f=open("27Bckab&7.txt")
mas=[int(q) for q in f][1:]
k=[0]*69
for i in mas:k[i%69]+=1
m=0
for i in range(69):
    m+=k[i]*(k[i]-1)//2
print(m)

#test
from itertools import *
k=0
for a,b in combinations(mas,2):
    if (a-b)%69==0:k+=1
print(k)