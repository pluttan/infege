f=open("27Bckab&2.txt")
mas=[int(q) for q in f][1:]
k7,k=0,0
for i in mas:
    if i%7==0:k7+=1
    else:k+=1
print(k*k7+k7*(k7-1)//2)

#test
from itertools import combinations
k=0
for a,b in combinations(mas,2):
    if (a*b)%7==0:k+=1
print(k)
