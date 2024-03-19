f=[int(q) for q in open("17ckab&14.txt")]
w=sum(f)/len(f)
m=[]
for a,b,c in zip(f,f[1:],f[2:]):
    if (a>w and b>w) or (a>w and c>w) or (c>w and b>w):
        m.append(a+b+c)
print(len(m),max(m))