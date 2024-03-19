f=open("27Ackab&6.txt")
mas=[int(q) for q in f][1:]
k=[0]*131
for i in mas:
    k[i%131]+=1
m=[k[i]*k[-i-1] for i in range(1,65)]
print(sum(m))

#test
from itertools import combinations
k=0
for a,b in combinations(mas,2):
    if (a+b)%131==0:k+=1
print(k)
