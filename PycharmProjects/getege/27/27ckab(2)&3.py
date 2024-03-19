f=open("27Bckab(2)&3.txt")
mas=[int(q) for q in f][1:]
p=[0]*10
m=0

for x in mas:
    for y in range(10):
        if (x*y)%5==0 and (x+y)%2!=0:m+=p[y]
    p[x%10]+=1
print(m)

#test
from itertools import *
k=0
for a,b in combinations(mas,2):
    if (a * b) % 5 == 0 and (a + b) % 2 != 0: k += 1
print(k)