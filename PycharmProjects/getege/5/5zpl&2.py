m=[]
for x in range(1,100):
    i=bin(x)[2:]
    i= i+i[-2]+i[-1] if i[-1]=="0" else "1"+i+"1"
    i=int(i,2)
    if i>130:m.append(int(i))
print(min(m))