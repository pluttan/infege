f=[int(d) for d in open("17kabdz&3.txt")]
q=max(f)
k,m=0,[]
for a,b,c in zip(f,f[1:],f[2:]):
    if a+b+c<=q:
        k+=1
        m.extend([a,b,c])
print(k,max(m)+min(m))