f=[int(q) for q in open("17ckab&15.txt")]
w=max([q for q in f if q%19==0])
m=[]
for a,b in zip(f,f[1:]):
    if a>w or b>w:m.append(a+b)
print(len(m),min(m))