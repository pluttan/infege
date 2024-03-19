f=open("24ckab(2)&12.txt").readlines()
k=0
for i in f:
    k1,k2=0,0
    for a,b,c in zip(i,i[1:],i[2:]):
        if a+b+c=="OAO":k1+=1
        if a+b+c=="AOA":k2+=1
    if k2>k1:k+=1
print(k)