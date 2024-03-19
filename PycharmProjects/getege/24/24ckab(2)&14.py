f=open("24ckab(2)&14.txt").readline()
k=0
for a,b,c,d,e in zip(f,f[1:],f[2:],f[3:],f[4:]):
    if a==e and b==d:k+=1
print(k)