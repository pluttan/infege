a=[]
for s1 in range(1,1000):
    for x1 in range(1,1000):
        s=s1
        x=x1
        s=100*s+x
        n=1
        while s<2021:
            s+=5*n
            n+=1
        if n==17:
            a.append(x1)
print(min(a))