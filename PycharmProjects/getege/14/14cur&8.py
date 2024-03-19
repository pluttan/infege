a = 25**56 + 5**138 - 5
k=0
while a>0:
    if a%5==4:k+=1
    a//=5
print(k)