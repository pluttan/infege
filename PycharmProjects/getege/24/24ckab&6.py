f=open("24ckab&6.txt").readline()
for i in range(97,1000):f=f.replace(chr(i)," ")
print(max(map(len,f.split())))