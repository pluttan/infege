f=[int(q) for q in open('17ckab&19.txt')]
m=[]
for a,b,c in zip(f,f[1:],f[2:]):
    if b>0 and str(b)[-1]=="9" and (a<0 or str(a)[-1]!="9") and (c<0 or str(c)[-1]!="9"):
        m.append(a+b+c)
print(len(m),max(m))