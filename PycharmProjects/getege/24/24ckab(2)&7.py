f=open("24ckab(2)&7.txt").readline()
k=0
for a,b,c,d in zip(f,f[1:],f[2:],f[3:]):
    if a=="G" and c=="M" and d=="E":k+=1
print(k)