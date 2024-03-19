mas=[int(q) for q in open("17zpl&4.txt")]
w=min([x for x in mas if x%6==0])
k=m=0
for a,b in zip(mas,mas[1:]):
    if a%w==0 and b%w==0:
        k+=1
        m=max(m,a+b)
print(k,m)