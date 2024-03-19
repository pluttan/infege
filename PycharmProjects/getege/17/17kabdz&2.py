f=[int(d) for d in open("17kabdz&2.txt")]
q=max(d for d in f if d%3==0)
k,m=0,0
for a,b in zip(f,f[1:]):
    if (a%3==0 and a!=q) or (b%3==0 and b!=q):
        k+=1
        m=max(m,a+b)
print(k,m)