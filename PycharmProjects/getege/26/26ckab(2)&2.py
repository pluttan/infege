f=open("26ckab(2)&2.txt")
s=f.readline()
mas=[int(x) for x in f]
mas.sort()

bd,sd=[],[]
while len(mas)>0:
    bd+=[mas.pop(len(mas)-1)]
    while sum(sd)<sum(bd):
        sd += [mas.pop(0)]
print(len(bd),len(sd))