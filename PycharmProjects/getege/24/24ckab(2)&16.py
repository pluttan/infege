f=open("24ckab(2)&16.txt").readline()
b=[]
for i in range(65,91):b.append(f.count(chr(i)))
print(max(b)-min(b),sep="")