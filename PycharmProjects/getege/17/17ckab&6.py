f=[int(q) for q in open("17ckab&6.txt")]
k=0
m=0
for a,b in zip(f,f[1:]):
    if (a+b)%3==0 and (a+b)%6!=0 and str(a*b)[-1]=='8':
        k+=1
        m=max(m,a+b)
print(k,m)