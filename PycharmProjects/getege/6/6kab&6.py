for i in range(1,100000):
    n=34
    s=i
    while n<=170:
        s+=120
        n+=23
    if len(str(s))==4:print(i)