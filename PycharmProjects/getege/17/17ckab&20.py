f=[int(q) for q in open("17ckab&20.txt")]
w=sum([sum(map(int,list(str(q)))) for q in f if q%35==0])
m=[]
for a,b in zip(f,f[1:]):
    if (a>w and b<w and hex(b)[-2]=="e" and hex(b)[-1]=="f") or (b>w and a<w and hex(a)[-2]=="e" and hex(a)[-1]=="f"):
        m.append(a+b)
print(len(m),min(m))