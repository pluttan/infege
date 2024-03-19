a=6*144**26+11*12**75-48
k=0
while a>0:
    k+=1 if a%12==11 else 0
    a//=12
print(k)