f=open("27Bckab&9.txt")
mas=[int(q) for q in f]
k=[0]*2000
for i in mas:
    try:
        k[2000-i]+=1
    except:pass
m=0
for i in range(1000):
    m+=k[i]*k[1999-i]
m+=k[1000]*(k[1000]-1)//2
print(m)

#test
from itertools import combinations
k=0
for a,b in combinations(mas,2):
    if (a+b)==2000:k+=1
print(k)