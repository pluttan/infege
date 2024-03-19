f=open("27Bckab(2)&4.txt")
mas=[int(i) for i in f][1:]
p=[0]*131
m=0

for x in mas:
    for y in range(131):
        if (x+y)%131==0:m+=p[y]
    p[x%131]+=1

print(m)
