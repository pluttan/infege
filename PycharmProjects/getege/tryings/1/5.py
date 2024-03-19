m=[]
for x in range(1,2000):
    i=bin(x)[2:]
    i= "10"+i+"10" if x%2==0 else "1"+i+"00"
    if int(i,2)>100:m.append(int(i,2))
print(min(m))