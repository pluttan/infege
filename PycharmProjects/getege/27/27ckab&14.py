from itertools import combinations
f=open("27Ackab&14.txt")
mas=[int(q) for q in f][1:]
m12=[q for q in mas if q%12==0]
m6=[q for q in mas if q%6==0 and q%12!=0]
m4=[q for q in mas if q%4==0 and q%12!=0 and q%6!=0]
m3=[q for q in mas if q%3==0 and q%4!=0 and q%12!=0 and q%6!=0]
m2=[q for q in mas if q%2==0 and q%3!=0 and q%4!=0 and q%12!=0 and q%6!=0]
m1=[q for q in mas if q%2!=0 and q%3!=0 and q%4!=0 and q%12!=0 and q%6!=0]
m12.sort();m6.sort();m4.sort();m3.sort();m2.sort();m1.sort()
q=m12[-4:]+m6[-4:]+m4[-4:]+m3[-4:]+m2[-4:]+m1[-4:]

m=0
for a,b,c,d in combinations(q,4):
    if (a*b*c*d)%12==0:m=max(m,a+b+c+d)
print(m)