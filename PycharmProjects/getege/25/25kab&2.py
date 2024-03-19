for x in range(100000000):
    for y in range(10):
        a=int("123"+str(x)+"567"+str(y))
        if a>10**9:break
        if a%169==0:
            print(a,a//169)