f=open("24.txt").readline()[::-1].replace("BB","$").replace("DD","$")
m=[];k=0
for i in f:
    if i=="$":k+=1
    else:m.append(k);k=0
print(max(m))
