a=3*16**2018-2*8**1018-3*4**1100-2**1050-2022
k=0
while a!=0:
    if a%4==3:k+=1
    a//=4
print(k)