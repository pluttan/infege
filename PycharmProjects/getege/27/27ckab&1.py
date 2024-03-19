f=open("27Bckab&1.txt")
mas=[int(q) for q in f][1:]
k2,k=0,0
for i in mas:
    if i%2==0:k2+=1
    else:k+=1
print(k2*(k2-1)//2+k*(k-1)//2)

#test
k=0
for j in range(len(mas)):
    for i in range(j+1,len(mas)):
        if (mas[j]+mas[i])%2==0:k+=1
print(k)