for x in range(1,100000):
    m=x
    k=0
    while m>0:
        m//=5
        k+=1
    if k<=4 and len(bin(x))>=7 and x%16==12:print(x)