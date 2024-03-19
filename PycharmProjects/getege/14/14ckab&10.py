a=5*216**1156-4*36**1147+6**1153-875
k=0
m=0
while a>0:
    k+=1 if a%6==5 else 0
    m += 1 if a % 6 == 0 else 0
    a//=6
print(k-m)
