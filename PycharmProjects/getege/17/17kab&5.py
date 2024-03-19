f=[int(d) for d in open("17kab&5.txt")]

q=max([d for d in f if d%19==0])
k,m=0,10000000000
for i in range(len(f)-1):
    if (f[i]>q or f[i+1]>q):
        k+=1
        m=min(m,f[i]+f[i+1])
print(k,m)