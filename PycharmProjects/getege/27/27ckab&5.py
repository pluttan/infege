f=open("27Bckab&5.txt")
mas=[int(q) for q in f][1:]
k19=0
for i in mas:
    if i%19==0:k19+=1
print(k19*(k19-1)*(k19-2)//6)

#test
from itertools import combinations
k=0
for a,b,c in combinations(mas,3):
    if a%19==0 and b%19==0 and c%19==0:k+=1
print(k)