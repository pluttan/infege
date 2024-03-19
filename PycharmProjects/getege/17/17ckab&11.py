f=[int(q)for q in open("17ckab&11.txt")]
k,m=0,10000
for a,b,c,d in zip(f,f[1:],f[2:],f[3:]):
    if a>b>c>d and (max(a,b,c,d)-min(a,b,c,d))>1000:
        k+=1
        m=min(m,a+b+c+d)
print(k,m)