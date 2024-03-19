k=0
for i in range(1,1000):
    s=i
    n=3
    while s*n<243:
        s//=3
        n*=9
        if n>1000:break
    if n==27:k+=1
    print(k)