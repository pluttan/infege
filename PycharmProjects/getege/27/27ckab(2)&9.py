mas=[int(i) for i in open("27Bckab(2)&9.txt")][1:]
k=k23=c=0
q=mas[:8]
mas=mas[8:]

for x in mas:
    if x%23==0:c+=k
    else: c+=k23

    k+=1
    if q[0]%23==0:k23+=1
    q.append(x)
    q.pop(0)
print(c)
