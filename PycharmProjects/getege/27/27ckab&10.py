f=open("27Bckab&10.txt")
mas=[int(q) for q in f]
nch=[q for q in mas if q%2!=0]
ch=[q for q in mas if q%2==0]
print(max(ch)+max(nch))

#test
from itertools import combinations
m=0
for a,b in combinations(mas,2):
    if (a+b)%2!=0:m=max(m,a+b)
print(m)