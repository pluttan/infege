a=51*7**12-7**3-22
k=0
while a>0:
    k+=a%7
    a//=7
print(k)