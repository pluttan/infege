x=open("24zpl&6.txt").readline()
while "PP" in x:x=x.replace("PP","P P")
print(max(map(len,x.split())))