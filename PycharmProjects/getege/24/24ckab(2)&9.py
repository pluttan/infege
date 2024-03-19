f=open("24ckab(2)&9.txt").readlines()
k=0
for i in f:
    k+=i.count("S")==i.count("X")
print(k)
