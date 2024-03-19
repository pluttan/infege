f=open("24ckab(2)&15.txt").readline()
b=[]
for i in range(65,91):b.append(f.count(chr(i)))
print(chr(b.index(max(b))+65),max(b),sep="")

