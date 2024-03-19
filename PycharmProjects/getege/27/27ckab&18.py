f=open("27Bckab&18.txt")
mas=[str(int(i)) for i in f]
q=[0]*10
for i in mas:
    for j in i:
        q[int(j)]+=1
print(min(q))