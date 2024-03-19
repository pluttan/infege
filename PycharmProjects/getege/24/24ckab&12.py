f=open("24ckab&12.txt").readline()
k=0
m=[]
for a,b in zip(f,f[1:]):
    if b>a:k+=1
    else:m.append(k+1);k=0
print(max(m))