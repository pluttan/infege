
for x in range(0,10):
    for y in range(0,10):
        a=int("1234"+str(x)+"57"+str(y)+"8")
        if a>10**9:break
        if a%17==0:print(a,a//17)