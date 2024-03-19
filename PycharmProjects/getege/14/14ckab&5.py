for x in range(1,10000):
    a=125**200-5**x+74
    k=0
    while a!=0:
        if a%5==4:k+=1
        a//=5
    if k==100:print(x)