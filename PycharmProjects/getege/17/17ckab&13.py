f=[int(q) for q in open("17ckab&13.txt")]
m=[]
for a,b in zip(f,f[1:]):
    if 50<=abs(a)+abs(b)<=200:
        m.extend([a,b])
print(len(m),min(m))