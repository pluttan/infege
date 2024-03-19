f=[int(q) for q in open("17ckab&9.txt")]
k,m=0,10000
for a,b,c in zip(f,f[1:],f[2:]):
    if (a%12==0 or b%12==0 or c%12==0) and a%3==0 and b%3==0 and c%3==0:
        q=(a+b+c)//3
        k+=1
        m=min(m,q)
print(k,m)