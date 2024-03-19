f=open("24ckab&10.txt").readline()
k,m=0,[]
for a,b in zip(f,f[1:]):
    if a!=b:k+=1
    else:m.append(k+1);k=0
print(max(m))