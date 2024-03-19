from itertools import combinations
f=open("27Bckab&13.txt")
mas=[int(q) for q in f][1:]
m=[[] for i in range(11)]
for i in mas:
    m[i%11].append(i)

q=[]
for i in range(11):
    m[i].sort()
    q.extend(m[i][:3])
m=100000000
for a,b,c in combinations(q,3):
    if (a+b+c)%11==0:m=min(m,a+b+c)
print(m)




# test
m=1000000000
for a,b,c in combinations(mas,3):
    if (a+b+c)%11==0:m=min(m,a+b+c)
print(m)