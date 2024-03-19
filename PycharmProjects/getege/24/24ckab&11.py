d=open("24ckab&11.txt").readline()
k=0
m=[]
for a,b in zip(d,d[1:]):
    if ord(a)<=ord(b):k+=1
    else: m.append(k+1);k=0
print(max(m))
