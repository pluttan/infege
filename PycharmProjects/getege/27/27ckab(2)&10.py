f=open("27Ackab(2)&10.txt")
q=[int(f.readline()) for i in range(5)][1:]
mas=[int(i) for i in f]
k0 = 0
k1 = 0
k0_13 = 0
k1_13 = 0
m=0
for x in mas:
    if x%26==0:m+=k1+k1_13
    elif x%13==0:m+=k0+k0_13
    elif x%2==0:m+=k1_13
    else:m+=k0_13
    r=q.pop(0)
    if r%26==0:k0_13+=1
    elif r%13==0:k1_13+=1
    elif r%2==0:k0+=1
    else:k1+=1
    q.append(x)
print(m)

#test
from itertools import combinations
k=0
for a in range(len(mas)):
    for b in range(a+1,len(mas)):
        if b-a==5 and\
                (mas[a]*mas[b])%13==0 and\
                (mas[a]+mas[b])%2==1:k+=1
print(k)