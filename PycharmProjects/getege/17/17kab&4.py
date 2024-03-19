f=[int(d) for d in open("17kab&4.txt")]

q=max([d for d in f if d%2==1])+min([d for d in f if d%2==1])
k,m=0,10000000000000
for i in range(len(f)-1):
    if (f[i]+f[i+1])%2==0 and f[i]+f[i+1]>q:
        k+=1
        m=min(f[i]+f[i+1],m)
print(k,m)