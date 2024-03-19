f=[int(d) for d in open("17kab&2.txt")]
q=sum(f)/len(f)
k=0
m=0
for i in range(len(f)):
    if f[i]<q and f[i+1]<q and (str(f[i])[-1]=="9" or str(f[i+1])[-1]=="9"):
        k+=1
        m=max(m,f[i]+f[i+1])
print(k,m)