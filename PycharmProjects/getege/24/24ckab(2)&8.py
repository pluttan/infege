f=open("24ckab(2)&8.txt").readline()
k=0
for a,b,c,d,e in zip(f,f[1:],f[2:],f[3:],f[4:]):
    if a==c==e=="A":k+=1
print(k)