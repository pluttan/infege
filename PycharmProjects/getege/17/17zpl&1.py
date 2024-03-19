mas=[int(q) for q in open("17zpl&1.txt")]
k=m=0
for a,b in zip(mas,mas[1:]):
    if a%3==0 or b%3==0:
        k+=1
        m=max(m,a+b)
print(k,m)