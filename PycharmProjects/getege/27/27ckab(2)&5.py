mas=[int(i) for i in open("27Bckab(2)&5.txt")][1:]
p=[0]*80
p5=[0]*80
m=0
for x in mas:
    for y in range(80):
        if (x+y)%80:
            if x>50000:
                m+=p[y]+p5[y]
            else:
                m+=p5[y]
    if x>50000:
        p5[x%80]+=1
    else:
        p[x % 80] += 1
print(m)

#test
from itertools import *
k=0
for a,b in combinations(mas,2):
    if (a+b)%80==0 and (a>50000 or b>50000):k+=1
print(k)

