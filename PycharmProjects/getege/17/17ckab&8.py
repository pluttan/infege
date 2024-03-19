f=[int(q) for q in open("17ckab&8.txt")]
k,m=0,0
for a,b,c in zip(f,f[1:],f[2:]):
    if (a*b*c)%7==0 and str(a+b+c)[-1]=="5":
        k+=1
        m=max(m,a+b+c)
print(k,m)