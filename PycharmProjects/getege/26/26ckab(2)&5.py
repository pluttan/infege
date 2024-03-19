from itertools import combinations
f=open("26ckab(2)&5.txt")
f.readline()
mas=[int(x) for x in f]
mass=set(mas)
k,m=0,0
for a,b in combinations(mas,r=2):
    if a%2!=b%2:
        if a+b in mass:
            k+=1
            m=max(m,a+b)
print(k,m)
