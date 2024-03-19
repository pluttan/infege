a=49**7+7**21-7
k=0
while a!=0:
    if a%7==6:k+=1
    a//=7
print(k)