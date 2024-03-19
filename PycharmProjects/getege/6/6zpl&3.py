for i in range(1,10000):
    s=i
    n=1
    while s<80:
        s+=7
        n*=3
    if n==27:print(i)