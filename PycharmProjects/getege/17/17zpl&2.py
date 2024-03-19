mas=[int(q) for q in open("17zpl&2.txt")]
w=max([x for x in mas if x%11==0])
k=m=0
for a,b in zip(mas,mas[1:]):
    if (a%11==0 or b%11==0) and (a+b)<=w:
        k+=1
        m=max(m,a+b)
print(k,m)