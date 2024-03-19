f=open("27Ackab&11.txt")
mas=[int(q) for q in f][1:]
k31=[q for q in mas if q%31==0]
k=[q for q in mas if q%31!=0]
k31.sort()
k.sort()
print(k31,k)
print(k31[0]*k[0])

#test
from itertools import combinations
m=100000000000000
for a,b in combinations(mas,2):
    if (a*b)%31==0:m=min(m,a*b)
print(m)