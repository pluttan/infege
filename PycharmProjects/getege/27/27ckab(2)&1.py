f=open("27Bckab(2)&1.txt")
mas=[int(q) for q in f][1:]
q=[0]*7
m=0
for i in mas:
    for y in range(7):
        if (i*y)%7==0:m+=q[y]
    q[i%7]+=1
print(m)

from itertools import combinations
k=0
for a,b in combinations(mas,2):
    if (a*b)%7==0:k+=1
print(k)
