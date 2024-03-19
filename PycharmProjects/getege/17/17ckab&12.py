f=[int(q) for q in open('17ckab&12.txt')]
k,m=0,-100000
for a,b in zip(f,f[1:]):
    if a+b>=100 and (a<0 or b<0):
        k+=1
        m=max(m,a*b)
print(k,m)