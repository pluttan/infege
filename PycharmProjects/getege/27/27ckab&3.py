f=open("27Bckab&3.txt")
mas=[int(q) for q in f][1:]
k65,k13,k5,k=0,0,0,0
for i in mas:
    if i%65==0:k65+=1
    elif i%13==0:k13+=1
    elif i%5==0:k5+=1
    else: k+=1
print(k65*(k65-1)//2+\
      k65*k13+\
      k65*k5+\
      k65*k+\
      k5*k13)

#test
from itertools import combinations
k=0
for a,b in combinations(mas,2):
    if (a*b)%65==0:k+=1
print(k)