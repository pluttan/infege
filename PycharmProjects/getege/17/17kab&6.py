f=[int(d) for d in open("17kab&6.txt")]

q=sum(f)/len(f)
k,m=0,0
for i in range(len(f)-2):
    if (int(f[i]>q) + int(f[i+1]>q) + int(f[i+2]>q))>=2:
        k+=1
        m=max(m,f[i]+f[i+1]+f[i+2])
print(k,m)