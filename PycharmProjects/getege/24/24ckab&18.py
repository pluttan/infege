f=open("24ckab&18.txt").readline().split("КОТ")
k=0
m=[]
for i in f:
    if i=="":k+=3
    else:m.append(k);k=0
print(max(m))