from itertools import combinations
f=open("26ckab(2)&4.txt")
mas=[int(x) for x in f][1:]
mas.sort()
m=1000000
k=0
for a,b in combinations(mas,r=2):
    arif=(a+b)//2 if (a+b)%2==0 else 0
    if mas[len(mas)//2-1]<arif and mas[3*len(mas)//4]>arif:
        m=min(m,arif)
        k+=1
print(k,m)