f=[int(q) for q in open("17ckab&7.txt")]
k,m=0,1000000
for a,b in zip(f,f[1:]):
    if (a+b)%7==0 and a*b>0:
        k+=1
        m=min(m,a*b)
print(k,m)