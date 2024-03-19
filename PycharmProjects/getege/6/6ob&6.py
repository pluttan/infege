k=0
for i in range(0,1000000):
    s=i
    n=10
    while s-n<1000:
        s+=n
        n+=5

    if n==80:k+=1
print(k)