f=[int(q) for q in open("17ckab&10.txt")]
k,m=0,0
for a,b,c in zip(f,f[1:],f[2:]):
    if (a%3==2 or b%3==2 or c%3==2):
        k+=1
        m+=min(a,b,c)
print(k,m)