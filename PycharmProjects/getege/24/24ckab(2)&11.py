f=open("24ckab(2)&11.txt").readlines()
k=0
for i in f:
    for a,b,c,d in zip(i,i[1:],i[2:],i[3:]):
        if a=="K" and c=="G" and d=="E":
            k+=1
            break
print(k)
