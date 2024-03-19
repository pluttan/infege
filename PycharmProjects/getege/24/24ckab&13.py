f=open("24ckab&13.txt").readline()
m=[]
k=""
for a,b in zip(f,f[1:]):
    if a>b:k+=b
    else:m.append(k);k=""
print(m[list(map(len,m)).index(max(list(map(len,m))))])