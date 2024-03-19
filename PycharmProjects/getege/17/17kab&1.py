
f=[int(d) for d in open("17kab&1.txt")]
mas=f.copy()
q=567
while q%6!=0:
    mas.remove(q)
    q=min(mas)
k=0
m=0
for i in range(len(f)-1):
    if f[i]%q==0 and f[i+1]%q==0:
        m=max(m,f[i]+f[i+1])
        k+=1
print(k,m)