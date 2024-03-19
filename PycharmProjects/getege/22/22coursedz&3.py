for i in range(1,1000000):
    x=i
    a=5*x+345
    b=5*x-807
    while a!=b:
        if b>0:
            if a>b:
                a-=b
            else:
                b-=a
        else:break
    else:
        if a==96:print(i)