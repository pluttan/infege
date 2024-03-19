f=open("24ckab(2)&10.txt").readlines()
k=0
for i in f:
    if (i.count("B")/i.count("A"))*100>=105:k+=1
print(k)