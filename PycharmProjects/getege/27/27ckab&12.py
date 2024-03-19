f=open("27Ackab&12.txt")
mas=[int(q) for q in f][1:]
a=[q for q in mas if q%23==0 and q%2==0]
b=[q for q in mas if q%23!=0 and q%2==0]
c=[q for q in mas if q%23==0 and q%2!=0]
d=[q for q in mas if q%23!=0 and q%2!=0]
a.sort();b.sort();c.sort();d.sort()
print(*map(len,[a,b,c,d]))
print(max(a[-1]+b[-1],c[-1]+d[-1]))

#test
from itertools import combinations
m=0
for a,b in combinations(mas,2):
    if (a+b)%2==0 and (a%23==0 or b%23==0):m=max(m,a+b)
print(m)
