f=[int(d) for d in open("17kabdz&1.txt")]
q=min([d for d in f if d%17==0])
k,m=0,0
for i in range(len(f)-1):
    if f[i]%q==0 or f[i+1]%q==0:
        k+=1
        m=max(m,f[i]+f[i+1])
print(k,m)