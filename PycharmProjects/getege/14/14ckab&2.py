a=3*16**8-4**5+3
k=0
while a!=0:
    if a%4==3:k+=1
    a//=4
print(k)