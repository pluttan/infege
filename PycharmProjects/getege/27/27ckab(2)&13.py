f=open("27Ackab(2)&13.txt")
k13=[[0]*13 for i in range(2)]
q=[int(f.readline()) for i in range(6)][1:]
mas=[int(i) for i in f]
m=0
for x in mas:
    if x%2==0:m+=k13[0][x%13]+k13[1][x%13]
    else:m+=k13[0][x%13]
    k13[q[0]%2][q.pop(0)%13]+=1
    q.append(x)
print(m)
