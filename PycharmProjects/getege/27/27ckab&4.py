f=open("27Bckab&4.txt")
mas=[int(q) for q in f][1:]
k5k2,n5k2,k5n2,n5n2=0,0,0,0
for i in mas:
    if i%5==0:
        if i%2==0:
            k5k2+=1
        else:
            k5n2+=1
    else:
        if i%2==0:
            n5k2+=1
        else:
            n5n2+=1
print(k5k2*k5n2+\
      k5k2*n5n2+\
      k5n2*n5k2)

#test
from itertools import combinations
k=0
for a,b in combinations(mas,2):
    if (a+b)%2!=0 and (a*b)%5==0:k+=1
print(k)
