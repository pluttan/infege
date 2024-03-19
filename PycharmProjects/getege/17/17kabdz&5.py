f=[int(d) for d in open("17kabdz&5.txt")]
q=max([d for d in f if d%2==1])
k,m=0,10000000
for a,b in zip(f,f[1:]):
    if 2*(a+b)>q:
        k+=1
        m=min(m,a+b)
print(k,m)