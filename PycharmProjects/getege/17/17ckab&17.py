f=[int(q) for q in open("17ckab&17.txt")]
w=min([q for q in f if str(q)[-1]=="4"])+max([q for q in f if str(q)[-1]=="4"])
m=[]
for a,b in zip(f,f[1:]):
    if a+b<w:
        m.append(a+b)
print(len(m),max(m))