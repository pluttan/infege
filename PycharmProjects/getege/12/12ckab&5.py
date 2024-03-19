for i in range(50,1,-1):
    a="6"*i
    while "66" in a:
        a=a.replace("66","1",1)
        a=a.replace("11","2",1)
        a=a.replace("22","6",1)
    if a=="21":print(i)