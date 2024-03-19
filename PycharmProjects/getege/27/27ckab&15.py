from itertools import combinations
f=open("27Bckab&15.txt")
mas=[int(q) for q in f][1:]

#test
m=0
for a,b in combinations(mas,2):
    if abs(a-b)%80==0:m=max(m,abs(a-b))
print(m)