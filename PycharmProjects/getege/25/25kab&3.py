for x in range(-1,100):
    for y in range(-1,100):
        if x==-1:x=""
        if y==-1:y=""
        a=int("12"+str(x)+"45"+str(y))
        if a>10**6:break
        if a%51==0:print(a,a//51)


