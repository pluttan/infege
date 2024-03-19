f=[int(d) for d in open("17kab&3.txt")]
print(f)
q=max([n for n in f if n%11==0])
m=0
k=0
for i in range(len(f)-1):
    if (f[i]%11==0 or f[i+1]%11==0) and f[i]+f[i+1]<=q:
        m=max(m,f[i]+f[i+1])
        k+=1
print(k, m)